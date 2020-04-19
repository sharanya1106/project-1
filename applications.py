import os
from flask import Flask, redirect, url_for, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from data import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# app.app_context().push()


db.init_app(app)
# db.create_all()

engine = create_engine(os.getenv("DATABASE_URL"))
Session = scoped_session(sessionmaker(bind=engine))
session = Session()

@app.route('/')
# def test():
#     return render_template("reg_page.html")

@app.route('/register', methods = ['POST', 'GET'])
def register_method():
    db.create_all()
    if request.method == 'POST':
        userdata = User(request.form["username"], request.form["pswd"])
        db.session.add(userdata)
        db.session.commit()
        # res = request.form
        # print(res)
        return render_template("reg_page.html")
    else:
        return render_template("reg_page.html")