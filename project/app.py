from cs50 import SQL
from flask import Flask, render_template, request, redirect, url_for
from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import smtplib
import os


app = Flask(__name__)

db = SQL("sqlite:///contacts.db")

# Configuración de SMTP
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")  # Este es el correo al que se enviarán las notificaciones

@app.before_request
def add_template_name():
    if request.endpoint:
        template_name = request.endpoint + '.html'
        request.template_name = template_name
    else:
        request.template_name = None

@app.route("/")
def index():
    return render_template("index.html", template_name = request.template_name)

@app.route("/about")
def about():
    return render_template("about.html", template_name = request.template_name)

@app.route("/projects")
def projects():
    return render_template("projects.html", template_name = request.template_name)

@app.route("/hobbie")
def hobbie():
    return render_template("hobbie.html", template_name = request.template_name)

@app.route("/contact")
def contact():
    return render_template("contact.html", template_name = request.template_name)

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        nombre = request.form["name"]
        email = request.form["email"]
        asunto = request.form["asunto"]
        mensaje = request.form["mensaje"]


    guardar = db

    guardar.execute("INSERT INTO Contactos(nombre,email,motivo,mensaje) VALUES (?,?,?,?)", nombre, email, asunto, mensaje)

    send_email_notification(nombre, email, asunto, mensaje)

    return redirect(url_for("contact"))


def send_email_notification(name, email, asunto, mensaje):
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = 'Nuevo mensaje de contacto'

    body = f"""
    Nuevo mensaje de contacto:

    Nombre: {name}
    Email: {email}
    Asunto: {asunto}
    Mensaje: {mensaje}
    """
    msg.set_content(body)
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
    except Exception as e:
        print(f"Error al enviar el correo: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)





