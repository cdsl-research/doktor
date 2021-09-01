from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import socket
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


def list_url():
    most_recent_three = fs.find().sort("uploadDate", -1).limit(50)
    res = []
    for grid_out in most_recent_three:
        res.append({
            "_id": str(grid_out._id),
            "filename": grid_out._file['filename'],
            "file_url": grid_out._file['file_url']
        })

    return res


@app.route("/list")
def index():
    pdflist = list_url()
    # TODO need to fix abstractive
    for p in pdflist:
        p['file_url'] = p['file_url'].replace(
            "doktor-upload:3000", "doktor.a910.tak-cslab.org:30010")

    # pdflist = ["http://doktor-upload:3000/" + word for word in pdflist]
    hostname = socket.gethostname()
    return jsonify(pdflist)


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
    app.run(host="0.0.0.0", port=4000, debug=True)
