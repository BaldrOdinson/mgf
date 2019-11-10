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

def build_num():
    with open (url_for('static', filename = 'build_info/build_no.txt'), 'r') as cur_num:
        bdl_num = cur_num.readline()
    with open (url_for('static', filename = 'build_info/build_no.txt'), 'w') as cur_num:
        if bdl_num == '':
            bdl_num = '1'
            cur_num.write(bdl_num)
    return bdl_num

@core.route('/')
def index():
    time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    l_num = load_num()
    bld_num = build_num()
    return render_template('index.html',
                                time = time,
                                load_num = l_num,
                                build_number = bld_num)
