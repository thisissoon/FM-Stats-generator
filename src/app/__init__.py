from flask import Flask


def create_app(config):
    app = Flask(__name__)
    try:
        app.config.from_pyfile('config/{}.py'.format(config))
    except IOError:
        raise IOError('Config {} does not exist'.format(config))

    from app.api.v1 import route
    app.register_blueprint(route, url_prefix='/api/1.0')

    return app
