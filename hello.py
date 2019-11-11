import flask
from flask_restplus import Resource, Api, fields

app = flask.Flask(__name__)
api = Api(app)

USERS = [
    {'id': 1, 'name': 'alice', 'email': 'alice@doe'},
    {'id': 2, 'name': 'bob', 'email': 'bob@doe'},
    {'id': 3, 'name': 'charlie', 'email': 'charlie@doe'}
]

USERMODEL = api.model(
    name='User',
    model={
        'id': fields.Integer(required=True),
        'name': fields.String(required=True, example="John Doe"),
        'email': fields.String(example="john@doe")
    }
)

@api.route('/users')
class UserList(Resource):

    @api.marshal_list_with(USERMODEL)
    def get(self):
        return USERS

if __name__ == '__main__':
    app.run()
