from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def index():
    # return '<div align=center><h1>Hello, World!</h1></div>'

from test_app.core.views import core
app.register_blueprint(core)
