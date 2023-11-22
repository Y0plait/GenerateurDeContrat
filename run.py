import os
from app import app

def run_app():
    """
    Runs the Flask application in development mode with debug enabled.
    """
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug=True)

if __name__ == '__main__':
    run_app()
