#!/usr/bin/python3
'''
Docstring
'''
if __name__ == "__main__":
    from flask import Flask, escape, request, abort, render_template
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

    @app.route("/number_template/<n>")
    def num_template(n, strict_slashes=False):
        if n.isdigit():
            return render_template("5-number.html", value=n)
        else:
            abort(404)

    @app.route("/number_odd_or_even/<n>")
    def evod_template(n, strict_slashes=False):
        if n.isdigit():
            if int(n) % 2 == 0:
                return render_template("6-number_odd_or_even.html",
                                       number=n, evod="even")
            else:
                return render_template("6-number_odd_or_even.html",
                                       number=n, evod="odd")
        else:
            abort(404)

    app.run(host='0.0.0.0', port='5000')
