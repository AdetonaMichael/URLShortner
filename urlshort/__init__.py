from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = "8kaklj0923nlnlenks0293ls23"

    from . import urlshort
    app.register_blueprint(urlshort.bp)
    return app