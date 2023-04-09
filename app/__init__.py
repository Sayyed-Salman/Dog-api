from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config=None):
    """Create an flask application."""

    app = Flask(__name__)
    api = Api(app)

    if config is None:
        config = 'app.config.DevelopmentConfig'

    app.config.from_object(config)

    db.init_app(app)

    with app.app_context():
        from app.models import Dog
        db.create_all()
    
    migrate.init_app(app, db)

    from app.routes import api_bp
    app.register_blueprint(api_bp)

    return app
