from config import DevConfig
from flask import Flask
from flask_login import current_user

from models import db
from controllers.catalog import catalog_blueprint
from controllers.main import main_blueprint
from .extensions import bcrypt, oid,login_manager, principals, rest_api, celery
from .controllers.rest.auth import AuthApi
from .controllers.rest.item import ItemApi
def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)
    bcrypt.init_app(app)
    oid.init_app(app)
    login_manager.init_app(app)
    principals.init_app(app)
    rest_api.add_resource(
    	ItemApi, 
    	'/api/item',
    	'/api/item/<int:item_id>',
    	endpoint='api'
    )
    rest_api.add_resource(
    	AuthApi, 
    	'/api/auth'
    )
    rest_api.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(catalog_blueprint)
    
    return app