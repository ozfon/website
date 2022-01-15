from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'peanut butter'

    from .views import views
    from .auth import auth
    from .tools import tools

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(tools, url_prefix='/tools')

    return app