import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/user/<int:id>')
def get_user(id):
    user = {"id": id, "name": "john", "email": "john@doe"}
    return render_template('template.html', user=user)

if __name__ == '__main__':
    app.run()
