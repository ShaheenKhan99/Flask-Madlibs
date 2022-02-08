from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = 'somethingSecret'

@app.route('/')
def show_form():
    """Generate and show form asking questions """

    prompts = story.prompts

    return render_template("form.html", prompts=prompts)

@app.route('/story')
def show_story():
    """Show generated story page """  
    text = story.generate(request.args)
    return render_template("story.html", text=text)


        