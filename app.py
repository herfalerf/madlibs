from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story, story_2


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def go_home():
    """Return to homepage"""
    return render_template("home.html")

@app.route('/story-form-1')
def go_form_1():
    """Navigate to story 1 entry form"""
    return render_template("story-1-form.html")

@app.route('/story-1')
def get_story_1():
    """Display madlib story"""
    choices = {"place":request.args["place"], "adjective":request.args["adjective"], "noun":request.args["noun"], "verb":request.args["verb"], "plural_noun":request.args["plural_noun"] }
    return render_template("story-1.html", madlib=story.generate(choices))

@app.route('/story-form-2')
def go_form_2():
    """Navigate to story 1 entry form"""
    return render_template("story-2-form.html")

@app.route('/story-2')
def get_story_2():
    """Display madlib story"""
    choices = {"place":request.args["place"], "adjective":request.args["adjective"], "noun":request.args["noun"], "verb":request.args["verb"], "plural_noun":request.args["plural_noun"] }
    return render_template("story-2.html", madlib=story_2.generate(choices))