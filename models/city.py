#!/usr/bin/python3
"""This Inititalizes City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """This constitutes a obj.
    Attr:
    state_id: state ID.
    name: city name.
    """
    state_id = ""
    name = ""
