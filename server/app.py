from flask import Flask, jsonify
from resources.models import db
import os
from settings import ProdConfig, DevConfig

def create_app(Configuration=DevConfig):
    app = Flask(__name__)
    app.config.from_object(Configuration or
                            os.environ.get('FLASK_CONFIG') or
                            'config')
    db.init_app(app)
    from resources import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    @app.route('/')
    def index():
        from resources import get_catalog as v1_catalog
        return jsonify(versions= {'v1': v1_catalog()})
    return app


if __name__ == '__main__':
    app = None
    if os.environ.get("FLASK_ENV") == 'prod':
        app = create_app(ProdConfig)
    else:
        app = create_app(DevConfig)
    app.run()
