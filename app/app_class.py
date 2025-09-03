from flask import Flask
from app.extensions import db
from app.routes import register_routes

class MyFlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = "random_secret_key"
        self.app.config.from_object("config.Config")
        self.app.config["JSON_SORT_KEYS"] = False

        db.init_app(self.app)
        self.db = db

        register_routes(self.app)
