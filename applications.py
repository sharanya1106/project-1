import os
from flask import Flask, redirect, url_for, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from data import *
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# app.app_context().push()


db.init_app(app)
# db.create_all()

engine = create_engine(os.getenv("DATABASE_URL"))
# Session = scoped_session(sessionmaker(bind=engine))
# session = Session()

@app.route('/')
def test():
    return redirect("/register")

@app.route("/admin")
def admin():
    allusersdata = User.query.all()
    return render_template("admin.html", admin = allusersdata)

@app.route('/register', methods = ['POST', 'GET'])
def register_method():
    db.create_all()
    if request.method == 'POST':
        userdata = User(request.form["username"], request.form["pswd"])
        user = User.query.filter_by(username=request.form['username']).first()
        if user is not None:            
            var = "Error: User already exists. Try with another Username or Register if you are new user"
            return render_template("reg_page.html", msg =var)
        db.session.add(userdata)
        db.session.commit()
        var = 'Registration Success'
        # res = request.form
        # print(res)

        return render_template("reg_page.html", msg1 = var)
    else:
        return render_template("reg_page.html")

@app.route("/auth", methods =['POST'])
def authenication():
    users = Users.query.filter_by(username = request.form['username']).first()
    if users is not None:
        if request.form['pswd'] == users.pswd:
            session["username"]=request.form["username"]
            return redirect("/homepage")
        else:
            var = "Incorrect Credentials"
            return render_template("reg_page.html", var = var)
    else:
        var = "You are not a registered user"
        return render_template("reg_page.html", var = var)


@app.route("/homepage")
def homepage():
    try:
        users = session["username"]
        return render_template("login.html")
    except:
        var = "login to view the homepage"
        return render_template("Registration.html",var = var)

@app.route("/logout")
def logout():
    try:
        users = session["username"]
        session.clear()
        var = "Logged out Successful"
        return render_template("reg_page.html",var = var)
    except:
        var = "You have to login to logout"
        return render_template("reg_page.html",var = var)

