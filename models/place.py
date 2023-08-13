#!/usr/bin/python3
"""This Initializes Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """This constitutes a place.
    Attr:
    city_id: City ID
    user_id: User ID
    name: Name of place
    description: Description of place
    number_rooms: Number of rooms of place
    number_bathrooms: Total number of bathrooms
    max_guest: Maximum number of guests
    price_by_night: Price by night
    latitude: Latitude of place
    longitude: Longitude of place
    amenity_ids: all Amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
