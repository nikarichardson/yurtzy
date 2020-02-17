from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy

import os
import json

#database_path = os.environ.get('DATABASE_URL', None)
database_path = os.environ.get('DATABASE_URL', None) #postgres://kwwzwozzasiqiw:8e70aed4e726e6e2d96cdf380525fa2884689070fdcda2daf3b0c389d879433f@ec2-18-213-176-229.compute-1.amazonaws.com:5432/df2ce01ne4r1gj
# os.environ['DATABASE_URL']
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = Column(db.Integer, primary_key=True)
  name = Column(db.String(120))
  catchphrase = Column(db.String(120))

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}
