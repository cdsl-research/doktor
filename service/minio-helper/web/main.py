from flask import *
import os
from doktor_health import health
from werkzeug.utils import secure_filename
import asyncio
import requests
import doktor_service as doktor

UPLOAD_FOLDER = os.path.dirname(__file__) + '/upload_temp'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__, static_folder="assets")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'hogehoge'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def show_page():
    return render_template(
        'index.html',
        msg='Hello, ',
        additional_msg="from Python")


@app.route("/upload")
def upload():
    return render_template(
        'upload.html',
        msg='Hello, ',
        additional_msg="from Python")


def service_upload(filename):
    # ★ポイント2
    fileName = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(fileName, 'rb') as fileDataBinary:
        files = {'pdf': (filename, fileDataBinary.read(), 'application/pdf')}

        # ★ポイント3
        url = 'http://doktor-upload:3000/web/upload'
        response = requests.post(url, files=files)
        fileDataBinary.close
        # print(response.status_code)

        print(response.content)
        return response.json()


@app.route("/uploading", methods=["POST"])
def uploading():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'pdf' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['pdf']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # loop = asyncio.get_event_loop()
            # loop.run_until_complete(asyncio.ensure_future(upload()))
            # loop.close()
            res = service_upload(filename)
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return res
            return redirect(url_for('show_list'))

    return '''
            <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''


# return render_template(
#     'uploading.html',
#     msg='Hello, ',
#     additional_msg="from Python")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route("/list")
def show_list():
    pdf_list = doktor.pdf_list()
    pdf_list
    return render_template(
        'list.html',
        list=pdf_list,
        additional_msg="from Python")


@app.route("/healthz")
def healthz():
    return render_template(
        'index.html',
        msg='Hello, ',
        additional_msg="from Python")


hashmap = {
    "key": "value"
}
app.run(host='0.0.0.0', port=5000, debug=True)
