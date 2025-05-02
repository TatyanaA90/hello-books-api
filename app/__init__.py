from flask import Flask
from .db import db, migrate
from .models import book
from .routes.book_routes import bp as books_bp
from flask_sqlalchemy import SQLAlchemy
import os

# def create_app():
#     app = Flask(__name__)
# # Database Migration: Connect the model seamlessly with our SQL database
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

# wave_5 
def create_app(config=None): # wave_6
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings
        app.config.update(config)
        
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(books_bp)

    return app