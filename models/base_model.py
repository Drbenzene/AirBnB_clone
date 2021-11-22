#!/usr/bin/python3
'''
Base Class
'''
from datetime import datetime as dt
import uuid
import models

class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs)
