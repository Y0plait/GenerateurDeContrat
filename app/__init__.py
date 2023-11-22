"""
This module initializes the Flask application and sets up the login manager.
"""
from flask import Flask
from flask_login import LoginManager
import logging as log
from app.routes.auth import User, UserQueries
from app.database.db_creation import check_db
from app.globals import ISDEBUG, LOG_LEVEL

log.basicConfig(filename='app.log', level=LOG_LEVEL, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
log.info("Starting application")

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.template_folder = '/home/y0plait/OneDrive_a.moulin@eleve.leschartreux.net/B1D/FormumaireV4_Python/app/templates'
app.config['SECRET_KEY'] = '8cf01dc52d36417b943728237ae7dcf3'

log.info("Application initialized")

login_manager = LoginManager(app)
login_manager.login_view = 'auth_bp.login'
login_manager.login_message = 'You must be logged in to access this page.'
login_manager.init_app(app)

log.info("Login manager initialized")

@login_manager.user_loader
def load_user(user_id):
    """
    Load a user from the database based on the given user_id.

    Args:
        user_id (int): The ID of the user to load.

    Returns:
        User or None: The loaded User object if the user is found in the database, None otherwise.
    """
    
    query = UserQueries('./app/database/database.sqlite')
    user_data = query.get_by_id(user_id)

    if user_data:
        user_id, first_name, last_name, email, password, creation_date = user_data
        return User(user_id=user_id, email=email, password=password, last_name=last_name, first_name=first_name, created_at=creation_date)
    else:
        return None  # Return None if user not found


from app.routes import auth, navigation

if ISDEBUG:
    from app.routes import debugging
    app.register_blueprint(debugging.debug_bp)

app.register_blueprint(auth.auth_bp)
app.register_blueprint(navigation.nav_bp)

check_db()
log.info("Database checked")

