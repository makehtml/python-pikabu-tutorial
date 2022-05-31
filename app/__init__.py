"""
Here should be some docstring for __init__.py
"""

import importlib
import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask

# from app.extensions import babel, csrf, db, executor, mail, migrate, security, session, toolbar
from app.extensions import db, migrate

# from app.filters import format_price, format_price_float, pluralize, round_dt
# from app.modules.core.mail import SecMailUtil
# from app.modules.core.models import user_datastore
from app.routes import bps
# from app.utils import url_for_icon
from config import config


def register_extensions(app: Flask) -> None:
    """Вызов метода 'init_app' для регистрации расширений
    в flask.Flask объект через параметр.
    """
    # babel.init_app(app)
    # csrf.init_app(app)
    # executor.init_app(app)
    db.init_app(app)
    # mail.init_app(app)
    migrate.init_app(app, db)
    # security.init_app(app, user_datastore, mail_util_cls=SecMailUtil)
    # session.init_app(app)
    # toolbar.init_app(app)


def register_blueprints(app: Flask) -> None:
    """Регистрация роутов.
    """
    for blueprint in bps:
        blueprint_module = importlib.import_module(
            f"app.modules.{blueprint['module']}.{blueprint['view']}")
        blueprint_instance = getattr(blueprint_module, blueprint["name"])
        app.register_blueprint(blueprint_instance, url_prefix=blueprint.get("prefix", None))


def create_app():
    """
    Функция, которая создает приложение
    """
    app = Flask(__name__)
    app.config.from_object(config[os.getenv("FLASK_ENV", "production")])

    if app.debug:
        import colorlog

        handler = colorlog.StreamHandler()

        werkzeug_logger = logging.getLogger("werkzeug")
        # coloredlogs.install(level="DEBUG", logger=werkzeug_logger)
        # coloredlogs.install(level="DEBUG", logger=app.logger)

        logger = colorlog.getLogger(__name__)
        logger.addHandler(handler)

        werkzeug_logger.setLevel(logging.DEBUG)
        app.logger.setLevel(logging.DEBUG)
        app.logger.info(f"{app.config['APP_NAME']} startup")

    if not os.path.exists("logs"):
        os.mkdir("logs")
    file_handler = RotatingFileHandler("logs/app.log", maxBytes=1048576, backupCount=10)
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s:%(message)s "
                                                "[in %(pathname)s:%(lineno)d]"))
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.DEBUG)

    # app.template_filter("format_price")(format_price)
    # app.template_filter("format_price_float")(format_price_float)
    # app.template_filter("pluralize")(pluralize)
    # app.template_filter("round_dt")(round_dt)
    # app.template_global("url_for_icon")(url_for_icon)

    register_extensions(app)
    register_blueprints(app)

    # os.makedirs(app.config.get("IMG_PRODUCTS_DIR"), exist_ok=True)

    return app
