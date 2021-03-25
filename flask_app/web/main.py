from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def show_page():
    return render_template('index.html', msg='Hello, ', additional_msg="from Python")

app.run(host='0.0.0.0',port=5000,debug=True)