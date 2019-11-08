import os
from flask import render_template, request, redirect, url_for, Blueprint
from time import gmtime, strftime

core = Blueprint('core', __name__, template_folder='templates/core')

@core.route('/')
def index():
    time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    build_number = str(os.environ[BUILD_NUMBER])
    return render_template('index.html',
                                time=time,
                                build_no=build_number)
