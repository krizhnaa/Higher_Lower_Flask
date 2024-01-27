import random
from flask import Flask

gen_num = random.randint(0, 9)
print(gen_num)

app = Flask(__name__)


@app.route("/")
def homepage():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:num>")
def check_num(num):
    if num < gen_num:
        return '<h1>Number is Too Low</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif num > gen_num:
        return '<h1>Number is Too High</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif num == gen_num:
        return '<h1>You Found me</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)