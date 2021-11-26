#!/usr/bin/python3
"""
A class of users that will inherit the Base Model
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """ Creating a class named User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__ = (self, *args, **kwargs):
        """
        Super will initialize the Parent Class
        """
        super().__init__(**kwargs)