##
## EPITECH PROJECT, 2020
## web_epytodo
## File description:
## run
##

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hallo_world():
    return 'Hello, World its test!' 

if __name__ == '__main__':
    app.run(debug=True)