from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from boto.s3.connection import S3Connection

import os
import json

# s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
database_path = os.environ.get('DATABASE_URL', None)
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
