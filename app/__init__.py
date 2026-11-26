from flask import Flask
from flask_migrate import Migrate

from app.config import Config
from app.config.database import db

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import user
    from app.routes.user_routes import user_bp

    app.register_blueprint(user_bp)

    return app