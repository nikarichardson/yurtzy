from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, abort,jsonify
import sys 
from flask_migrate import Migrate
import os
import json

# database_path = os.environ.get('DATABASE_URL', None)
database_path = os.environ['DATABASE_URL']
# database_path = 'postgres://kwwzwozzasiqiw:8e70aed4e726e6e2d96cdf380525fa2884689070fdcda2daf3b0c389d879433f@ec2-18-213-176-229.compute-1.amazonaws.com:5432/df2ce01ne4r1gj'
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

  id = Column(db.Integer, primary_key=True)

  ## Required Fields
  name = Column(db.String(120),unique=True)
  address = db.Column(db.String(120),nullable=False)
  distance_from_city = Column(db.Integer,nullable=False)
  closest_city = db.Column(db.String(120),nullable=False) 

  ## Boolean Fields/Optional Fields
  image = Column(db.String(120))  
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

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}
