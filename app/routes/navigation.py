from flask import Blueprint, render_template, redirect, url_for, request

nav_bp = Blueprint('nav_bp', __name__, template_folder='../../templates/navigation', static_folder='../../static')

@nav_bp.route('/', methods=['GET'])
@nav_bp.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@nav_bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')