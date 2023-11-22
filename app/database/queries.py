import sqlite3
from datetime import datetime
from app import globals

class UserQueries:
    """
    A class that provides methods to interact with the 'users' table in the database.
    """

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_all(self):
        """
        Retrieves all users from the 'users' table.

        Returns:
            A list of tuples representing the users.
        """

        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def get_by_id(self, id):
        """
        Retrieves a user by their ID from the 'users' table.

        Args:
            id: The ID of the user.

        Returns:
            A tuple representing the user.
        """

        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def get_by_email(self, email):
        """
        Retrieves a user by their email from the 'users' table.

        Args:
            email: The email of the user.

        Returns:
            A tuple representing the user.
        """

        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return self.cursor.fetchone()

    def get_by_last_name(self, last_name):
        """
        Retrieves a user by their last name from the 'users' table.

        Args:
            last_name: The last name of the user.

        Returns:
            A tuple representing the user.
        """

        self.cursor.execute("SELECT * FROM users WHERE last_name = ?", (last_name,))
        return self.cursor.fetchone()
    
    def get_by_first_name(self, first_name):
        """
        Retrieves a user by their first name from the 'users' table.

        Args:
            first_name: The first name of the user.

        Returns:
            A tuple representing the user.
        """

        self.cursor.execute("SELECT * FROM users WHERE first_name = ?", (first_name,))
        return self.cursor.fetchone()

    def insert(self, user):
        """
        Inserts a new user into the 'users' table.

        Args:
            user: An object representing the user.

        Returns:
            The ID of the inserted user.
        """

        self.cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)", (user.first_name, user.last_name, user.email, user.password))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_password(self, user):
        """
        Updates the password of a user in the 'users' table.

        Args:
            user: An object representing the user.

        Returns:
            The ID of the updated user.
        """

        self.cursor.execute("UPDATE users SET password = ? WHERE id = ?", (user.password, user.id))
        self.conn.commit()
        return self.cursor.lastrowid

    def update(self, user):
        """
        Updates the details of a user in the 'users' table.

        Args:
            user: An object representing the user.

        Returns:
            The ID of the updated user.
        """

        self.cursor.execute("UPDATE users SET first_name = ?, last_name = ?, email = ?, password = ? WHERE id = ?", (user.first_name, user.last_name, user.email, user.password, user.id))
        self.conn.commit()
        return self.cursor.lastrowid

    def delete(self, id):
        """
        Deletes a user from the 'users' table.

        Args:
            id: The ID of the user to be deleted.

        Returns:
            The ID of the deleted user.
        """

        self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        self.conn.commit()
        return self.cursor.lastrowid

    def last_insert_rowid(self):
        """
        Retrieves the ID of the last inserted row.

        Returns:
            The ID of the last inserted row.
        """

        return self.cursor.lastrowid

    def check_password(self, user, password):
        """
        Checks if the password is correct for a given user.

        Args:
            user: An object representing the user.
            password: The password to check.

        Returns:
            True if the password is correct, False otherwise.
        """
        # user[0] is the id
        self.cursor.execute("SELECT password FROM users WHERE id = ?", (user[0],))
        dbPass = self.cursor.fetchone()
        return dbPass[0] == password

    def close(self):
        """
        Closes the database connection.
        """

        self.conn.close()