"""Flask application factory."""

import os
from flask import Flask

from .config import Config


def create_app(config_class=Config):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app = Flask(
        __name__,
        static_folder=os.path.join(root_dir, "static"),
        template_folder=os.path.join(root_dir, "templates"),
    )
    app.config.from_object(config_class)

    from . import routes
    routes.register_routes(app)

    return app
