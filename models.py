from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, abort,jsonify
import sys 
from flask_migrate import Migrate
import os
import json

database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    migrate = Migrate(app, db)
    db.init_app(app)
    db.create_all()


'''
Campsite
Have title and release year
'''
class Campsite(db.Model):  
  __tablename__ = 'Campsite'

  id = Column(db.Integer, primary_key=True,unique=True)
  #id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)

  ## Required Fields
  name = Column(db.String(120),unique=True)
  address = db.Column(db.String(120),nullable=False)
  distance_from_city = Column(db.Integer,nullable=False)
  closest_city = db.Column(db.String(120),nullable=False) 

  ## Boolean Fields/Optional Fields
  image = Column(db.String(1000),default=None)  
  website = Column(db.String(500),default=None)
  description = db.Column(db.String(5000),default=None) 
  costs = db.Column(db.Integer,default=0) 
  yurts_and_cabins = db.Column(db.Boolean,default=False) 
  bathrooms = db.Column(db.Boolean,default=False) 
  parking = db.Column(db.Boolean,default=False) 
  ada_access = db.Column(db.Boolean,default=False) 
  campfires = db.Column(db.Boolean,default=False) 
  showers = db.Column(db.Boolean,default=False) 
  wifi = db.Column(db.Boolean,default=False) 
  trash_bins = db.Column(db.Boolean,default=False) 
  picnic_area = db.Column(db.Boolean,default=False) 
  pets_allowed = db.Column(db.Boolean,default=False)
  potable_water = db.Column(db.Boolean,default=False)  
  rv_parks = db.Column(db.Boolean,default=False) 
  hiking = db.Column(db.Boolean,default=False) 
  camping = db.Column(db.Boolean,default=False) 
  biking = db.Column(db.Boolean,default=False) 
  kayaking = db.Column(db.Boolean,default=False) 
  swimming = db.Column(db.Boolean,default=False) 
  cooking_grills = db.Column(db.Boolean,default=False) 
  hunting = db.Column(db.Boolean,default=False) 

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

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
  query_filter()
    updates a new model into a database
    the model must exist in the database
  '''
  #def query_filter(filter):
  #  selection = db.session.query(Campsite).filter(Campsite.id == campsite_id).all() 
  #  return selection 

  '''
  format()
    returns a formatted object containing the values 
    of the model 
  '''
  def format(self):
    return {
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
      'hunting': self.hunting}


