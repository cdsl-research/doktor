from flask import *
import os
from doktor_health import health
from werkzeug.utils import secure_filename
import asyncio
import requests

UPLOAD_FOLDER = 'upload_temp'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__, static_folder="assets")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'hogehoge'

def service_upload(filename):
    fileName = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    fileDataBinary = open(fileName, 'rb').read()
    files = {'pdf': (filename, fileDataBinary, 'application/pdf')}

    url = 'http://doktor-upload:3000/web/upload'
    response = requests.post(url, files=files)
    # print(response.status_code)
    print(response.content)
    return response.json()

def pdf_list():
    url = 'http://doktor-search:4000/list'
    response = requests.get(url)
    # print(response.status_code)
    print(response.content)
    return response.json()


