from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required

gen_bp = Blueprint('gen_bp', __name__, template_folder='../../templates/navigation', static_folder='../../static')

@gen_bp.route('/', methods=['GET'])
@gen_bp.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@gen_bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@gen_bp.route('/protected')
@login_required
def protected():
    return ('Protected')