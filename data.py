from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__="user_details"
    username=db.Column(db.String, primary_key = True)
    pswd = db.Column(db.String, nullable= False)
    timestamp = db.Column(db.DateTime(timezone=True))

    def __init__(self, username, pswd):
        self.username = username
        self.pswd = pswd
        self.timestamp= datetime.now()
