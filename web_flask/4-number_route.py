#!/usr/bin/python3
'''
Docstring
'''
if __name__ == "__main__":
    from flask import Flask, escape, request, abort

    app = Flask(__name__)

    @app.route('/')
    def hello(strict_slashes=False):
        return("Hello HBNB!")

    @app.route('/hbnb')
    def hbnb(strict_slashes=False):
        return("HBNB")

    @app.route("/c/<text>")
    def text_c(text, strict_slashes=False):
        text = text.replace("_", " ")
        return("C {content}".format(content=text))

    @app.route("/python/")
    @app.route("/python/<text>")
    def text_python(text="is cool", strict_slashes=False):
        text = text.replace("_", " ")
        return("Python {content}".format(content=text))

    @app.route("/number/<n>")
    def hbnb_num(n, strict_slashes=False):
        num = n
        if (num.isdigit()):
            return ("{} is a number".format(num))
        else:
            abort(404)

    app.run(host='0.0.0.0', port='5000')
