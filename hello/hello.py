import flask
from flask_restplus import Resource, Api, fields
from .api import api

app = flask.Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run()
