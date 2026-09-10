import pickle
import base64
from flask import Flask, request, send_file

app = Flask(__name__)


@app.route("/session")
def session():
    blob = request.args.get("s")
    return str(pickle.loads(base64.b64decode(blob)))


@app.route("/report")
def report():
    name = request.args.get("name")
    return send_file("/srv/reports/" + name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
