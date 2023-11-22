from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user

nav_bp = Blueprint('nav_bp', __name__, template_folder='../../templates/navigation', static_folder='../../static', static_url_path='/static/nav')

@nav_bp.route('/', methods=['GET'])
@nav_bp.route('/index', methods=['GET'])
def index():
    try:
        if current_user.email is not None:
            return render_template('index.html', user=current_user.email)
    except AttributeError:
        return render_template('index.html', user="Aonymous User")

@nav_bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')