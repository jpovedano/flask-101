import flask
from flask import render_template, send_file

app = flask.Flask(__name__)

@app.route('/static/<path:path>')
def get_static_file(path):
    return send_file(path)

@app.route('/users/<int:id>')
def get_user(id):
    users = [{"id": id, "name": "john", "email": "john@doe"}]
    return render_template('template.html', users=users)

@app.route('/users')
def get_users():
    users = [
        {"id": 1, "name": "alice", "email": "alice@doe", "enabled": True},
        {"id": 2, "name": "bob", "email": "bob@doe", "enabled": True},
        {"id": 3, "name": "charlie", "email": "charlie@doe", "enabled": False},
    ]
    return render_template('template.html', users=users)

if __name__ == '__main__':
    app.run()
