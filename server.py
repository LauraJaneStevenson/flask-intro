"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['dumb','annoying','rude','stupid','crazy']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        Hi! This is the home page.
        <a href="/hello">hello</a>
      </body>

    
    </html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your first name? <input type="text" name="firstname">
          What's your last name? <input type="text" name="lastname"><br>
         Select compliment <select name = "compliment">
          <option value="smart">smart</option>
          <option value="a boss">a boss</option>
          <option value="talented">talented</option>
         </select>
          Are you an engineer?<input type="radio" value="yes" name="isengineer">Yes
          <input type="radio" value="no" name="isengineer">No
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route("/greet")
def greet_person():
    """Get user by name."""

    first = request.args.get("firstname")
    last = request.args.get("lastname")
    isengineer = request.args.get("isengineer")
    compliment = request.args.get("compliment")

    greeting = "Hi, {} {}! I think you're {}!".format(first,last, compliment)


    if isengineer=="yes":
      greeting = "Hi, {} {}! I think you're a {} engineer!".format(first,last, compliment)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        {}

      </body>
    </html>
    """.format(greeting)


@app.route("/hi")
def say_hi():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <br>
          <input type="radio" value="compliment" name="compordiss">Complimented
          <input type="radio" value="insult" name="compordiss">Dissed
          <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/diss")
def diss_person():
    """Get user by name."""
    # player = request.args.get("person")
    
    compordiss = request.args.get("compordiss")
    selection = ""
    if compordiss == 'compliment':
       selection = """Select compliment level<select name = "level">
          <option value="nice">nice</option>
          <option value="nicer">nicer</option>
          <option value="nicest">nicest</option>
         </select>"""

    if compordiss == 'insult':
     selection = """Select diss level<select name = "level">
        <option value="mean">mean</option>
        <option value="meaner">meaner</option>
        <option value="meanest">meanest</option>
       </select>"""



    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        <form action="/compordiss">
        {}
        <input type="submit" value="submit">
        </form?
      </body>
    </html>
    """.format(selection)

@app.route("/compordiss")
def compordiss():


  level = request.args.get("level")

  compordiss_dict{
      'mean': ['boring','dull','crazy']
      'meaner': ['stupid','lazy','dumb']
      'meanest': ['horrible','disgusting','dumb blonde']
      'nice': ['kind','cool'] 
  }






if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
