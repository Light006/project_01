from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app=Flask(__name__)
    app.debug=True

    bootstrap = Bootstrap(app)
    
    from . import views
    app.register_blueprint(views.bp)

    return app