import os
import subprocess
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy import exc
from models import setup_db, Campsite

def create_app(test_config=None):

	app = Flask(__name__)
	setup_db(app)
	CORS(app)

	@app.route('/')
	def hello_greeting():
		"""
		excited = os.environ['EXCITED']
		greeting = "Hello" 
		#person = Person(name="Maria", catchphrase="hello!")
		#person.insert()
		if excited == 'true': 
			greeting = greeting + "!!!!!"
			return greeting 
		"""
		return "Welcome to the Yurtzy backend site! 🏕️ "   
		

	"""
	Gets all campsites organized under listings of nearest urban centers.
	""" 
	@app.route('/campsites', methods=['GET'])
	def get_campsites():
		try:
			selection = Campsite.query.order_by(Campsite.id).all()

			if len(selection) == 0:
				abort(404)

			campsites = []
			for campsite in selection:
				campsites.append(campsite.format())

			return jsonify({
				'success': True,
				'campsites': campsites
			})

		except:
			abort(422)


	"""
	Retrieves the campsite with the given campsite id.
	"""
	@app.route('/campsites/<int:campsite_id>', methods=['GET'])
	def get_campsites_by_id(campsite_id):
		try:
			selection = Campsite.query.get(campsite_id)
		
			if selection is not None:
				return jsonify({
					'success': True,
					'campsite': selection.format()
				})
			else:
				abort(404)

		except:
			abort(422)
	

	"""
	Adds a new campsite to the database. 
	"""

	@app.route('/campsites', methods=['POST'])
	def add_campsite():
		body = request.get_json()

		# if no form data
		if body is None:
			abort(404)

		# retrieve form data
		name = body.get('name',False) 
		address = body.get('address',False) 
		distance_from_city = body.get('distance_from_city',False) 
		closest_city = body.get('closest_city',False) 
		image = body.get('image',False)  
		website = body.get('website',False) 
		description = body.get('description',False) 
		costs = body.get('costs',False) 
		yurts_and_cabins = body.get('yurts_and_cabins',False)  
		bathrooms = body.get('bathrooms',False) 
		parking = body.get('parking',False)  
		ada_access = body.get('ada_access',False) 
		campfires = body.get('campfires',False) 
		showers = body.get('showers',False) 
		wifi = body.get('wifi',False)  
		trash_bins = body.get('trash_bins',False) 
		picnic_area = body.get('picnic_area',False) 
		pets_allowed = body.get('pets_allowed',False) 
		potable_water = body.get('potable_water',False) 
		rv_parks = body.get('rv_parks',False) 
		hiking = body.get('hiking',False) 
		camping = body.get('camping',False) 
		biking = body.get('biking',False) 
		kayaking = body.get('kayaking',False) 
		swimming = body.get('swimming',False)  
		cooking_grills = body.get('cooking_grills',False)  
		hunting = body.get('hunting',False) 

		

		campsite = Campsite(name=name,address=address,distance_from_city=distance_from_city,
			closest_city=closest_city,image=image,website=website,description=description,
			costs=costs)

		campsite.insert() 

		return jsonify({
			'success': True,
			'name': campsite.format() 
		}) 

		"""
		try:
			campsite = Campsite(name=name,address=address,distance_from_city=distance_from_city,
			closest_city=closest_city,image=image,website=website,description=description,
			costs=costs,yurts_and_cabins=yurts_and_cabins,bathrooms=bathrooms,
			parking=parking,ada_access=ada_access,campfires=campfires,showers=showers,
			wifi=wifi,trash_bins=trash_bins,picnic_area=picnic_area,pets_allowed=pets_allowed,
			potable_water=potable_water,rv_parks=rv_parks,hiking=hiking,camping=camping,
			biking=biking,kayaking=kayaking,swimming=swimming,cooking_grills=cooking_grills,
			hunting=hunting)
			campsite.insert()

			campsites = []
			for campsite in selection:
				campsites.append(campsite.format())

			return jsonify({
				'success': True,
				'campsites': campsites
			})
		

		except:
			abort(422)
		"""
	
	"""
	Allows users to edit the given campsite.
	"""
	@app.route('/campsites/<int:campsite_id>', methods=['PATCH'])
	def update_campsite(campsite_id):
		return "Not implemented!"


	"""
	Delete campsite with the given id. 
	"""
	@app.route('/campsites/<int:campsite_id>', methods=['DELETE'])
	def delete_campsite(campsite_id):
		try:
			selection = Campsite.query.get(campsite_id)

			if selection is None:
				abort(404)

			selection.delete()

			return jsonify({
				'success': True,
				'delete': campsite_id,
			})

		except:
			abort(422)


	# Error Handling
	'''
	422: Unprocessable entity.
	'''
	@app.errorhandler(422)
	def unprocessable(error):
		return jsonify({
			"success": False,
			"error": 422,
			"message": "unprocessable"
		}), 422


	'''
	404 Error: Resource cannot be found.
	'''


	@app.errorhandler(404)
	def not_found(error):
		return jsonify({
			"success": False,
			"error": 404,
			"message": "not found"
		}), 404


	'''
	401 Error: User lacks valid authentication credentials for the desired resource
	'''


	@app.errorhandler(401)
	def unauthorized(error):
		return jsonify({
			"success": False,
			"error": 401,
			"message": "unauthorized"
		}), 401


	'''
	403 Error: Access to resource is forbidden.
	'''


	@app.errorhandler(403)
	def forbidden(error):
		return jsonify({
			"success": False,
			"error": 403,
			"message": "forbidden"
		}), 403


	'''
	500 Error: Arises in other cases.
	'''


	@app.errorhandler(500)
	def unprocessable(error):
		return jsonify({
			"success": False,
			"error": 500,
			"message": "internal server error"
		}), 500

	return app

app = create_app()

if __name__ == '__main__':
	app.run()
