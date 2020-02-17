import os
import subprocess
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import json
from models import setup_db, Campsite

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def hello_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        #person = Person(name="Maria", catchphrase="hello!")
        #person.insert()
        if excited == 'true': 
            greeting = greeting + "!!!!!"
            return greeting 
        

    @app.route('/campsites', methods=['GET'])
    def get_campsites():
        """
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        #person = Person(name="Maria", catchphrase="hello!")
        #person.insert()
        if excited == 'true': 
            greeting = greeting + "!!!!!"
            return greeting #+ person.name 
        """
        return "Not implemented!"

    @app.route('/campsites/<int:campsite_id>', methods=['GET'])
    def get_campsites_by_id(campsite_id):
        return "Not implemented!"


    @app.route('/campsites', methods=['POST'])
    def add_campsite():
        return "Not implemented!"


    @app.route('/campsites', methods=['PATCH'])
    def update_campsite():
        return "Not implemented!"


    @app.route('/campsites/<int:campsite_id>', methods=['DELETE'])
    def delete_campsite(campsite_id):
        return "Not implemented!"


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
