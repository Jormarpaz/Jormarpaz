# My own website/portfolio
## Video Demo:  <[URL HERE](https://youtu.be/Db6KyYO7Sno)>
### Description:

As I am in my second/third year of university, I need to start talking with companies
for internships or "prácticas" as we call it in Spain. I thought that this might be a
very cool way of using things learned during the Course and also a good thing for my
image in the actual market, not everybody is interested in doing things like this
and it may set the difference with other candidates at the interviews or in linkdn.


First of all, I started by creating the templates in html, using jinja(something that
I discovered with David and that makes things very very easy rather than using the same
header over and over again). After that, and asking my girlfriend for some advice with
the visuals, I coded the brain... I mean, "app.py", where basically I change the template
to be used if something is clicked and other low-profile things that change while using the
web. But, my favourite and most difficult part was the contact page. I used some pages like
"UI Elements" or even Instagram for inspiration with the Social Media buttons. I also
asked chat-gpt if he knew of some easy way to connect the page with the mail, but he gave
me very weird and complicated answers... At the end "Stackoverflow" keeps being the king
and there I found my answer. Oh, I must not forgot about the DB, "contacts", just there for
those that might prefer me to be the one stablishing contact via mail, so they just have to
write their name, mail, subject and what they need.

Now, one part at the time.

####App.py####

First of all I imported everything I needed for the project, including "dotenv", that, as you can see in the first part of the code, I used to keep secret my password and my username, its
an easy and cool way to keep things away from others eyes. After that I have the functions to
redirect the different .html when needed. And, at last, the email part, where, checking that
its a POST method, the web requires the name, mail, subject and text. Then saves it in the DB
and calls the function to send the mail using all this information plus the password and user
that I keep in the .env.

####contacts.db####

Where I keep the information about each person that contacts me.

####Layout.html####

As its name says, it is the main .html and from where the others are built.
I had to add Bootstrap references for some implementations and a font-family
for the text. The script right below serves to keep the person in the same page if they click
the button of the page where they are, so instead of reloading, the page just moves to the
top. After that its the main block that each .html will change and lately the buttons to
change the page, spheres that took me a while to comprehend.

####Index.html####

First page and my introduction for anyone that gets in here. Very simple and integrated within
the main block of jinja

####About.html####

Second page of the project, here I talk mainly of my life and studies, including some lists
and a table and a few paragraphs, not that much, all this in a main block.

####Proyects.html####

Third page and here is where I show all my projects, most of them from the CS50x course but
a some of them also from university, mainly in java and sql. Again, integrated using jinja,
a few paragraphs and done.

####Hobbie.html####

Fourth page and where I talk about my hobbies outside code and computer science. With a few images of my favourite games styled in a cool way so they change from grey to their
actual colours when the mouse goes across them.

####Contact.html####

Fifth and last page, this is my favourite because of its complexity and the visual-help I needed from my gf. Hee I use a lot of spans to create the ilusion for the Social Media icons
that are visible on the top of the web. Right below them its the contact formulary, just in case someone wants me to make the first step and also the contact information, my mail and
phone number just in case anyone wants to contact me first. This information is added to the DB
so If I loose the mail or the information, I can check it there.


####Styles.css####

I got to do almost everythin myself, nothing out of the normal, but I checked some ideas in from instagram and, while being helped by chatgpt, y got (in my opinion) to create a visually
satisfying website, most probably not the best, but here it is.
