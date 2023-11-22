import sqlite3
from datetime import datetime
from app import globals

def check_db():
    """
    Creates the 'users' table if it doesn't exist in the database.
    """
    
    
    conn = sqlite3.connect(globals.DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    if len(tables) == 0:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT,
                    password TEXT,
                    creation_date DATE
                )
            """)
            
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            if count == 0:
                cursor.execute("INSERT INTO users (first_name, last_name, email, password, creation_date) VALUES (?, ?, ?, ?, ?)", (globals.DEFAULT_USER_LAST_NAME, globals.DEFAULT_USER_FIRST_NAME, globals.DEFAULT_USER_EMAIL,globals.DEFAULT_USER_PASSWORD, datetime.now()))
                conn.commit()
                
        except Exception as e:
            raise Exception(e)
                
    else:
        pass
    