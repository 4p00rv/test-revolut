from flask_sqlalchemy import SQLAlchemy
import logging
from datetime import datetime

db = SQLAlchemy()

def init_db(app):
    """ Initialies the SQLAlchemy app """
    User.init_db(app)

class User(db.Model):
    app = None
    logger = logging.getLogger(__name__)

    # Table structure
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    dateOfBirth = db.Column(db.DateTime, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def init_db(cls, app):
        cls.logger.info("Initializing database")
        cls.app = app
        db.init_app(app)
        app.app_context().push()
        db.create_all()

    @classmethod
    def calculate_days(cls, now, dob):
        #dob = datetime.strptime(dob, "%Y-%m-%d")
        date1 = datetime(now.year, dob.month, dob.day+1)
        date2 = datetime(now.year+1, dob.month, dob.day+1)

        return ((date1 if date1 > now else date2) - now).days

