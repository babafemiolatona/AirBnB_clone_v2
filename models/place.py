#!/usr/bin/python3
""" Place Module for HBNB project that inherit the baseModel and Base"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place that is identified by many attributes """
    __tablename__ = "places"
    city_id = (Column(String(60), ForeignKey('cities.id'), nullable=False))
    user_id = (Column(String(60), ForeignKey('users.id'), nullable=False))
    name = (Column(String(128), nullable=False))
    description = (Column(String(1024)))
    number_rooms = (Column(Integer, default=0, nullable=False))
    number_bathrooms = (Column(Integer, default=0, nullable=False))
    max_guest = (Column(Integer, default=0, nullable=False))
    price_by_night = (Column(Integer, default=0, nullable=False))
    latitude = (Column(Float))
    longitude = (Column(Float))
    reviews = (relationship("Review", backref="place", cascade="delete"))
    amenity_ids = []
