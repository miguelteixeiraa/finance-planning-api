from flask import Flask
from db.MainStorageProvider import MainStorageProvider


app = Flask(__name__)


@app.route("/")
def hello():
    db = MainStorageProvider()
    db.deleteAll({"test": True})

    return db.get("62c20ecfe8b232790b3cf1e0")
