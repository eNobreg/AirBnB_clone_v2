#!/usr/bin/python3
'''
Docstring
'''
if __name__ == "__main__":
    from flask import Flask, escape, request

    app = Flask(__name__)

    @app.route('/')
    def hello(strict_slashes=False):
        return("Hello HBNB!")

    @app.route('/hbnb')
    def hbnb(strict_slashes=False):
        return("HBNB")
    app.run(host='0.0.0.0', port='5000')
