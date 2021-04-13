from flask import *
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import socket
from werkzeug.utils import secure_filename
import asyncio
import requests
import os
import io
import bson
import uuid
import gridfs

UPLOAD_FOLDER = 'upload_temp'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/dev"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'hogehoge'

mongo = PyMongo(app)
db = mongo.db
fs = gridfs.GridFS(db)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'pdf' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['pdf']
        # if user does not select file, browser also
        # submit an empty part without filename
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))

    hostname = socket.gethostname()
    return jsonify(
        message="Welcome to Tasks app! I am running inside {} pod!".format(hostname))


@app.route("/web/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'pdf' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['pdf']
        # if user does not select file, browser also
        # submit an empty part without filename
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        fileDataBinary = open(save_path, 'rb').read()
        id = bson.objectid.ObjectId(str(uuid.uuid4()).replace("-", "")[:24])
        args = {'filename': file.filename, '_id': id, 'file_url': "http://doktor-upload:3000/pdf/" + str(id)}
        res = fs.put(file, file=fileDataBinary, **args)
        result = {
            '_id': str(id),
            'filename': filename,
            'file_url': "http://doktor-upload:3000/pdf/" + str(id)
        }

        print(id)
        return jsonify(data=result)


@app.route("/pdf/list")
def get_all_tasks():
    tasks = fs.find()
    data = []
    for task in tasks:
        item = {
            "id": str(task["_id"]),
            "file_name": task["file_name"],
            # "pdf": task["pdf"]
        }
        data.append(item)
    return jsonify(
        data=data
    )


@app.route("/pdf/<id>", methods=["GET"])
def get_task(id):
    get_obj = fs.get(bson.objectid.ObjectId(id))
    print(get_obj.filename)  # b'Hello, World!'
    # response = make_response(get_obj.file)
    # response.headers.set('Content-Type', 'application/pdf')
    # response.headers.set(
    #     'Content-Disposition', 'attachment', filename='%s.pdf' % id)
    # return response

    return send_file(
        io.BytesIO(get_obj.file),
        mimetype='application/pdf',
        attachment_filename='%s.pdf' % id)


@app.route("/task", methods=["POST"])
def create_task():
    data = request.get_json(force=True)
    db.task.insert_one({"task": data["task"]})
    return jsonify(
        message="Task saved successfully!"
    )


@app.route("/task/<id>", methods=["PUT"])
def update_task(id):
    data = request.get_json(force=True)["task"]
    response = db.task.update_one({"_id": ObjectId(id)}, {
        "$set": {"task": data}})
    if response.matched_count:
        message = "Task updated successfully!"
    else:
        message = "No Task found!"
    return jsonify(
        message=message
    )


@app.route("/task/<id>", methods=["DELETE"])
def delete_task(id):
    response = db.task.delete_one({"_id": ObjectId(id)})
    if response.deleted_count:
        message = "Task deleted successfully!"
    else:
        message = "No Task found!"
    return jsonify(
        message=message
    )


@app.route("/tasks/delete", methods=["POST"])
def delete_all_tasks():
    db.task.remove()
    return jsonify(
        message="All Tasks deleted!"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
