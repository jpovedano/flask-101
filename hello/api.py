import flask
from flask_restplus import Resource, Api, fields

api = Api(title="User Database API")

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
    @api.response(200, 'Sucess')
    def get(self):
        """Get the list of users."""
        return USERS

    @api.expect(USERMODEL, validate=True)
    @api.response(200, 'Sucess')
    @api.response(303, 'Already existing')
    def post(self):
        """Add a new user."""
        payload = flask.request.get_json()
        for user in USERS:
            if user['id'] == payload['id']:
                return {"message": "Record already existed"}, 303
        USERS.append(payload)
        return {"message": "Record updated"}, 200

@api.route('/users/<int:id>')
class User(Resource):
    @api.marshal_with(USERMODEL)
    @api.response(200, 'Success')
    @api.response(404, 'User not found')
    def get(self, id):
        for user in USERS:
            if user['id'] == id:
                return user
        # If not found, raise a 404
        flask.abort(404)