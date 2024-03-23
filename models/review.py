#!/urs/bin/python3
"""
The Review class definition
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class definition of a Review
    Attributes
        name: city's name
    """
    place_id = ""
    user_id = ""
    text = ""
