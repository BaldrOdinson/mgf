import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,  static_url_path=f'/{basedir}/static')

from test_app.core.views import core
app.register_blueprint(core)
