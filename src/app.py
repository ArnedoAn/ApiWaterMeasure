from flask import Flask
from routes import route
import os

PORT = os.environ.get("PORT")

app = Flask(__name__)


def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    app.register_blueprint(route.mainep)
    app.register_error_handler(404, page_not_found)
    app.run(port=PORT, debug=True)
