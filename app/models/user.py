from flask_login import UserMixin
from datetime import datetime

from app.database.queries import UserQueries
from app.globals import DB_PATH

class User(UserMixin):
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        created_at (datetime): The date and time when the user account was created.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, user_id, email, password, created_at, first_name=None, last_name=None):
        self.id = user_id
        self.email = email
        self.password = password
        self.created_at = created_at
        self.first_name = first_name
        self.last_name = last_name
        self._is_authenticated = False
        self._is_active = True
        self._is_anonymous = False

    @property
    def is_active(self):
        return True
    
    def is_authenticated(self):
        return self._is_authenticated
    
    def is_anonymous(self):
        return self._is_anonymous
    
    def get_id(self):
        return self.id

    def create_account(self):
        """
        Creates a new user account in the database.

        Returns:
            bool: True if the account creation is successful, False otherwise.
        """
        query = UserQueries(DB_PATH)
        state = query.insert(self) 
        query.close()
        return state

    def update_profile(self, new_data):
        """
        Updates user profile data in the database.

        Args:
            new_data (dict): The updated user profile data.

        Returns:
            bool: True if the profile update is successful, False otherwise.
        """
        query = UserQueries(DB_PATH)
        state = query.update(self)
        query.close()
        return state

    def change_password(self):
        """
        Changes the user's password in the database.

        Returns:
            bool: True if the password change is successful, False otherwise.
        """
        query = UserQueries(DB_PATH)
        state = query.update_password(self)
        query.close()
        return state

    def delete_account(self):
        """
        Deletes the user's account from the database.

        Returns:
            bool: True if the account deletion is successful, False otherwise.
        """
        query = UserQueries(DB_PATH)
        state = query.delete(self.id)
        query.close()
        return state

    def serialize(self):
        """
        Converts user object to a dictionary for session storage or API responses.

        Returns:
            dict: The serialized user object.
        """
        return {
            'id': self.id,
            'email': self.email,
            'created_at': str(self.created_at),
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    @staticmethod
    def deserialize(data):
        """
        Creates a user object from a dictionary (e.g., retrieved from session data).

        Args:
            data (dict): The dictionary containing user data.

        Returns:
            User: The deserialized user object.
        """
        return User(
            user_id=data['id'],
            email=data['email'],
            password=None,  # Password should not be stored in session data
            created_at=datetime.strptime(data['created_at'], '%Y-%m-%d %H:%M:%S'),
            first_name=data['first_name'],
            last_name=data['last_name']
        )