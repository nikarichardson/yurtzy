import os
import subprocess
from flask import Flask
from flask_cors import CORS
from models import setup_db

def create_app(test_config=None):

    app = Flask(__name__)
    subprocess.call(['./setup.sh'])
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        person = Person(name="Sabrina", catchphrase="yo!")
        if excited == 'true': 
            greeting = greeting + "!!!!!"
            return greeting + person.name 


    @app.route('/coolkids')
    def be_cool():
        return "Be cool, be coooool! You're almost a FSND grad!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
