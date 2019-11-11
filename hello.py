import flask
from flask import render_template_string

app = flask.Flask(__name__)

template="""
<html>
<body>
<h1>Hello User {{ id }}</h1>
</body>
</html>
"""

@app.route('/user/<int:id>')
def get_user(id):
    return render_template_string(template, id=id)

if __name__ == '__main__':
    app.run()
