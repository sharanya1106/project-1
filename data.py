from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__="user_details"
    username=db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable= False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
