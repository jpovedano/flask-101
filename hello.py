import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/about')
def about():
    return "About"

@app.route('/user/<int:id>')
def get_user(id):
    return "Hello user #{userid}".format(userid=id)

if __name__ == '__main__':
    app.run()
