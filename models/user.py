#!/usr/bin/python3
'''A class for our users'''
from models.base_model import BaseModel


class User(BaseModel):
    '''this is the class for our users'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
