#!/urs/bin/python3
"""
The User class definition
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class definition of a User
    Attributes
        email: user's email
        password: user's password
        first_name: user's first name
        last_name: user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
