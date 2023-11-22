from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User, UserQueries
from app.globals import DB_PATH

auth_bp = Blueprint('auth_bp', __name__, template_folder='../../templates/auth', static_folder='../../static')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate user credentials
        user_queries = UserQueries(DB_PATH)
        user = user_queries.get_by_email(email)
        
        print(f"email : {email}")
        print(f"password : {password}")
        print(f"user : {user}")
    
        if user_queries.check_password(user, password):
            login_user(User(user_id=user[0], email=user[3], password=user[4], first_name=user[1], last_name=user[2], created_at=user[5]))
            print(f"User logged in {user[3]}")
            return redirect(url_for('nav_bp.index'))

        print("Invalid email or password")
        return render_template('login.html', error='Invalid email or password')

    else:
        return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('nav_bp.index'))

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    """
    Register a new user.

    This function handles the registration process for a new user. It receives the email and password from the request
    form, checks if the email is already registered, creates a new user if it is not, and logs in the new user.

    Returns:
        A redirect response to the index page.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        

        # Check if the email is already registered
        user_queries = UserQueries(DB_PATH)
        existing_user = user_queries.get_by_email(email)

        if existing_user:
            return render_template('register.html', error='Email already registered')

        # Retrieve the last user ID from the database
        last_user = int(user_queries.last_insert_rowid())

        # Create a new user
        new_user = User(user_id=last_user+1, email=email, password=password, first_name=first_name, last_name=last_name, created_at=datetime.now())
        new_user.create_account()

        # Log in the new user
        login_user(new_user)

        return redirect("/")
    else:
        return render_template('register.html')

@auth_bp.route('/protected')
@login_required
def protected():
    return f'Hello, {current_user.email}! This is a protected route.'

