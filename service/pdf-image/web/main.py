from flask import Flask, render_template, request
from doktor_health import health

app = Flask(__name__)


@app.route("/")
def show_page():
    return render_template(
        'index.html',
        msg='Hello, ',
        additional_msg="from Python")

## http://pdf-image/create
@app.route("create")
def create_pdf_image():

    ###
    # ここでファイルをオープン f = open(pdfのリンク)
    # ここにpdfからJPGにするコード
    # ここにDBにJPGを保存するコード
    ###

    return jpeg_path


@app.route("/healthz")
def healthz():
    return render_template(
        'index.html',
        msg='Hello, ',
        additional_msg="from Python")


app.run(host='0.0.0.0', port=5000, debug=True)
