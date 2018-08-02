from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [

    {

    'author': 'Osvin Alaphat',

    'title': 'Blog post 1',

    'content': 'First post content',

    'date_posted': 'July 18, 2018'

    },

    {

    'author': 'Alvin Alaphat',

    'title': 'Blog post 2',

    'content': 'Second post content',

    'date_posted': 'July 17, 2018'

    },

]



@app.route("/")
@app.route("/home")
def home():

    return render_template('home.html', posts=posts)



@app.route("/about")
def about():

    return render_template('about.html', title='About')



@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():

    form = LoginForm()

    return render_template('login.html', title='Login', form=form)
