from flask import Blueprint, request

mainep = Blueprint("test", __name__, url_prefix="/api/test")

@mainep.route("/", methods=["GET"])
def index():
    return "Hello world!"


@mainep.route("/data", methods=["GET", "POST"])
def data():
    return "Data"
