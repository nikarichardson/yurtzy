from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
from flask import url_for, abort, jsonify
import sys
from flask_migrate import Migrate
import os
import json

database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()

'''
setup_db(app) binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    migrate = Migrate(app, db)
    db.init_app(app)
    db.create_all()


'''
Campsite Model
'''


class Campsite(db.Model):
    __tablename__ = 'Campsite'

    id = Column(db.Integer, primary_key=True, unique=True)
    # Required Fields
    name = Column(db.String(120), unique=True)
    address = db.Column(db.String(120), nullable=False)
    distance_from_city = Column(db.Integer, nullable=False)
    closest_city = db.Column(db.String(120), nullable=False)

    # Boolean Fields/Optional Fields
    image = Column(db.String(1000))
    website = Column(db.String(500))
    description = db.Column(db.String(5000))
    costs = db.Column(db.Integer)
    yurts_and_cabins = db.Column(db.Boolean)
    bathrooms = db.Column(db.Boolean)
    parking = db.Column(db.Boolean)
    ada_access = db.Column(db.Boolean)
    campfires = db.Column(db.Boolean)
    showers = db.Column(db.Boolean)
    wifi = db.Column(db.Boolean)
    trash_bins = db.Column(db.Boolean)
    picnic_area = db.Column(db.Boolean)
    pets_allowed = db.Column(db.Boolean)
    potable_water = db.Column(db.Boolean)
    rv_parks = db.Column(db.Boolean)
    hiking = db.Column(db.Boolean)
    camping = db.Column(db.Boolean)
    biking = db.Column(db.Boolean)
    kayaking = db.Column(db.Boolean)
    swimming = db.Column(db.Boolean)
    cooking_grills = db.Column(db.Boolean)
    hunting = db.Column(db.Boolean)

    def __init__(self, name, address, distance_from_city,
                 closest_city, image, website, description,
                 costs, yurts_and_cabins, bathrooms, parking,
                 ada_access, campfires, showers, wifi,
                 trash_bins, picnic_area, pets_allowed,
                 potable_water, rv_parks, hiking, camping,
                 biking, kayaking, swimming, cooking_grills,
                 hunting):
        self.name = name
        self.address = address
        self.distance_from_city = distance_from_city
        self.closest_city = closest_city
        self.costs = costs
        self.description = description
        self.website = website
        self.image = image
        self.yurts_and_cabins = yurts_and_cabins
        self.bathrooms = bathrooms
        self.parking = parking
        self.ada_access = ada_access
        self.campfires = campfires
        self.showers = showers
        self.wifi = wifi
        self.trash_bins = trash_bins
        self.picnic_area = picnic_area
        self.pets_allowed = pets_allowed
        self.potable_water = potable_water
        self.rv_parks = rv_parks
        self.hiking = hiking
        self.camping = camping
        self.biking = biking
        self.kayaking = kayaking
        self.swimming = swimming
        self.cooking_grills = cooking_grills
        self.hunting = hunting

    '''
    insert()
    inserts a new model into a database
    the model must have a unique name
    the model must have a unique id or null id
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
    deletes a new model into a database
    the model must exist in the database
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
    updates a new model into a database
    the model must exist in the database
    '''
    def update(self):
        db.session.commit()

    '''
    format()
    returns a formatted object containing the values
    of the model
    '''
    def format(self):
        return
        {
            'id': self.id,
            'name': self.name,
            'website': self.website,
            'address': self.address,
            'distance_from_city': self.distance_from_city,
            'closest_city': self.closest_city,
            'image': self.image,
            'description': self.description,
            'costs': self.costs,
            'yurts and cabins': self.yurts_and_cabins,
            'bathrooms': self.bathrooms,
            'parking': self.parking,
            'ada access': self.ada_access,
            'campfires': self.campfires,
            'showers': self.showers,
            'wifi': self.wifi,
            'trash bins': self.trash_bins,
            'picnic area': self.picnic_area,
            'pets allowed': self.pets_allowed,
            'potable water': self.potable_water,
            'rv parks': self.rv_parks,
            'hiking': self.hiking,
            'camping': self.camping,
            'biking': self.biking,
            'kayaking': self.kayaking,
            'swimming': self.swimming,
            'cooking_grills': self.cooking_grills,
            'hunting': self.hunting
        }
