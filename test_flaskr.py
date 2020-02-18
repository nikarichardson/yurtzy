import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Campsite 


class CampsiteTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia" 
        self.database_path = "postgres://kwwzwozzasiqiw:8e70aed4e726e6e2d96cdf380525fa2884689070fdcda2daf3b0c389d879433f@ec2-18-213-176-229.compute-1.amazonaws.com:5432/df2ce01ne4r1gj"
        setup_db(self.app, self.database_path)

        campsite = Campsite(name="Trillum Lake Test",address="Highway 26 Government Camp, Oregon 97028",distance_from_city=50,
            closest_city="Portland",image="https://tinyurl.com/slcnop9",
            website="https://www.fs.usda.gov/recarea/mthood/recarea/?recid=53634",
            description="Incredible views of Mount Hood.", costs=50,yurts_and_cabins=False,
            bathrooms=True,parking=True,ada_access=True,campfires=True,showers=True,
            wifi=False,trash_bins=True,picnic_area=True,pets_allowed=True,
            potable_water=True,rv_parks=True,hiking=True,camping=True,
            biking=True,kayaking=True,swimming=True,cooking_grills=True,
            hunting=False)

        campsite.insert()
        self.id = campsite.id 

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""

        # delete test campsite
        test = Campsite.query.get(self.id) 
        test.delete() 

    """
    Test get campsites endpoint. 
    """
    def test_get_campsites(self):
        res = self.client().get('/campsites')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['campsites'])
        self.assertTrue(len(data['campsites']))

    """
    Test get campsite by id endpoint.
    """
    def test_get_campsites_by_id(self):
        res = self.client().get('/campsites/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['campsites'])
        self.assertTrue(len(data['campsites']))


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()