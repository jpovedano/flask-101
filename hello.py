import flask
from flask_restplus import Resource, Api

app = flask.Flask(__name__)
api = Api(app)

USERS = [
    {'id': 1, 'name': 'alice', 'email': 'alice@doe'},
    {'id': 2, 'name': 'bob', 'email': 'bob@doe'},
    {'id': 3, 'name': 'charlie', 'email': 'charlie@doe'}
]

@api.route('/users')
class UserList(Resource):

    def get(self):
        return USERS

if __name__ == '__main__':
    app.run()
