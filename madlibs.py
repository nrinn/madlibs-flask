from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    game_approve = request.args.get("yesno")
    
    if game_approve == "no":
        return render_template("goodbye.html")
    elif game_approve == "yes":
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    person = request.args.get("person")
    adjective = request.args.get("adjectives")
    color = request.args.get("color")
    noun = request.args.get("noun")
    insult = request.args.get("insult")
    checkbox1 = request.args.getlist("verb")

    print checkbox1, "BECCA"

    return render_template("madlib.html", color = color, adjective = adjective, insult = insult, person = person, noun = noun, checkbox = checkbox1)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
