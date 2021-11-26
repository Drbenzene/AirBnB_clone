#!/usr/bin/python3
"""
contains the entry point of the command interpreter.
"""
import cmd
from shlex import split

import models
from models.base_models import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    The class that implement the console
    """
    prompt = "(hbnb)"
    storage = models.storage
    


