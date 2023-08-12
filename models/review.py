#!/usr/bin/python3
""" inherit from BaseModel """


from models.base_model import BaseModel


class Review(BaseModel):
    """Review  inherit from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
