from flask import *
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import socket
from werkzeug.utils import secure_filename
import asyncio
import requests
import os
import uuid

UPLOAD_FOLDER = 'upload_temp'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/dev"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'hogehoge'

mongo = PyMongo(app)
db = mongo.db


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
        id = uuid.uuid4()
        result = {'id': id, 'file_url': filename}
        return jsonify(data=result)


@app.route("/tasks")
def get_all_tasks():
    tasks = db.task.find()
    data = []
    for task in tasks:
        item = {
            "id": str(task["_id"]),
            "task": task["task"]
        }
        data.append(item)
    return jsonify(
        data=data
    )


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
