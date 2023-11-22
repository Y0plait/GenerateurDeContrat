from flask import Blueprint, render_template
from app.globals import DB_PATH
import sqlite3

debug_bp = Blueprint('debug_bp', __name__, template_folder='../../templates/debugging', static_folder='../../static')

@debug_bp.route('/debug/<command>', methods=['GET'])
def sql_prompt(command=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if command:
        print(command)
        cursor.execute(command)
        conn.commit()
        return render_template('sql_prompt.html', command=command, output=cursor.fetchall())
    elif command is "":
        return render_template('sql_prompt.html')
    else:
        return render_template('sql_prompt.html')