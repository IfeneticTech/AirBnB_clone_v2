#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Prints Web """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Prints Web """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Prints a char C followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ prints Python, followed by the value of the text variable,
    with default value of text: is cool """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ the number route """
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
