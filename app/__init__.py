from flask import Flask
#from .routes.hello_world_routes import hello_world_bp    # uses for hello_word_routes
from .routes.book_routes import books_bp


def create_app():
    app = Flask(__name__)

    # Register Blueprints here
    #app.register_blueprint(hello_world_bp)     # uses for hello_word_routes
    app.register_blueprint(books_bp)

    return app