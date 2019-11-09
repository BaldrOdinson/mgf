import os
from flask import render_template, request, redirect, url_for, Blueprint
from time import gmtime, strftime

core = Blueprint('core', __name__, template_folder='templates/core')

def load_num():
    with open (url_for('static', filename = 'load_num.txt'), 'r') as cur_num:
        c_num = cur_num.readline()
    if c_num == '':
        c_num = '1'
        with open (url_for('static', filename = 'load_num.txt'), 'w') as cur_num:
            cur_num.write(c_num)
    else:
        c_num = str(int(c_num) + 1)
        with open (url_for('static', filename = 'load_num.txt'), 'w') as cur_num:
            cur_num.write(c_num)
    return c_num

@core.route('/')
def index():
    time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    l_num = load_num()
    return render_template('index.html',
                                time = time,
                                load_num = l_num)
