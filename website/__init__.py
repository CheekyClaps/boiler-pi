import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='sukkel',
        ##DATABASE=os.path.join(app.instance_path, 'website.sqlite'),
    )
    
    from .views import views
    app.register_blueprint(views, url_prefix="/")

    return app
