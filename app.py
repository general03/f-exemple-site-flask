from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/other")
def hello_other():
    page = request.args.get('page', default = 1, type = int)
    return f"<p>Hello, Other!</p><p>Page : {page}<:p>"


@app.route("/exp")
def exp():
    value = int(request.args.get('value'))
    return f"<p>Exposant 2 de {value} : {pow(value, 2)}</p>"
