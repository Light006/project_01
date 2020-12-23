from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app=Flask(__name__)
    app.debug=True

    bootstrap = Bootstrap(app)
    
    from . import views
    app.register_blueprint(views.bp)
    from . import about
    app.register_blueprint(about.bp)
    from . import contact
    app.register_blueprint(contact.bp)
    from . import services
    app.register_blueprint(services.bp)

    return app