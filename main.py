from loadScript import load

load()


from flask import Flask
from TypeService import TypeService
from bson import ObjectId, json_util


app = Flask(__name__)


@app.route("/")
def hello():
    services = TypeService()

    # testing
    return json_util.dumps(services.getTypes())
