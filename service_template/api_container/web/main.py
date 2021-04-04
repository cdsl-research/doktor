from flask import Flask, render_template, json
from doktor_health import health

app = Flask(__name__)


@app.route("/")
def show_page():
    return render_template(
        'index.html',
        msg='Hello, ',
        additional_msg="from Python")


@app.route("/healthz")
def healthz():
    my_health = health.Health(status=health.HealthStatus.GREEN,
                              description="It works")
    return json.jsonify(my_health.to_dict())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
