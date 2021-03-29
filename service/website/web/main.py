from flask import Flask, render_template
from doktor_health import health

app = Flask(__name__, static_folder="assets")


@app.route("/")
def show_page():
    return render_template(
        'index.html',
        msg='Hello, ',
        additional_msg="from Python")

@app.route("/generic")
def generic():
    return render_template(
        'generic.html',
        msg='Hello, ',
        additional_msg="from Python")

@app.route("/elements")
def elements():
    return render_template(
        'elements.html',
        msg='Hello, ',
        additional_msg="from Python")

@app.route("/healthz")
def healthz():
    return render_template(
        'index.html',
        msg='Hello, ',
        additional_msg="from Python")


app.run(host='0.0.0.0', port=5000, debug=True)
