# standard routes for the website, where users can actually go, not authentication
from flask import Blueprint, render_template # blueprint of our website, has a bunch of routes

views = Blueprint('views', __name__) # sets up blueprint

# function will run whenever we go to the main page of the website
@views.route('/') # decorator
def home():
    return render_template("index.html")

@views.route('/about')
def webapp():
    return render_template("about.html")

@views.route('/impact')
def impact():
    return render_template("impact.html")

@views.route('/inequalities')
def inequalities():
    return render_template("inequalities.html")

@views.route('/process')
def process():
    return render_template("process.html")

@views.route('/reflection')
def reflection():
    return render_template("reflection.html")

@views.route('/swiping')
def swiping():
    return render_template("swiping.html")

@views.route('/closet')
def closet():
    return render_template("closet.html")

@views.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

@views.route('/sources')
def sources():
    return render_template("sources.html")