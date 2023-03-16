#!/usr/bin/python3
'''A class for our reviews'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''instatntiates our class'''
    place_id = ''
    user_id = ''
    name = ''
