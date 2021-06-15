from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

# local import
from server.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    config = app_config[config_name]
    logging.basicConfig(
        level=config.LOGLEVEL,
        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
    )

    app.logger.info("Config: %s" % app_config[config_name].__dict__)
    app.config.from_object(config)
    app.logger.info("Current env: %s"% app.env)
    #app.config.from_pyfile('config.py')
    db.init_app(app)

    return app
