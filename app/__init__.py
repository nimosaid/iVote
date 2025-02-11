from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()


photos = UploadSet('photos', IMAGES)

def create_app(config_name):

    app = Flask(__name__)


    # Initializing flask extensions
    bootstrap.init_app(app)
    login_manager.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    # configure UploadSet
    # configure_uploads(app,photos)
    
    # Will add the views and forms

    return app