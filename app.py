from flask import Flask, render_template
import os, mysql.connector 
from dotenv import load_dotenv

load_dotenv ()
from database_connection import get_connection


def create_app ():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")   


    @app.route("/",methods=["GET"])
    def dashboard():
        return render_template("exemple_dashboard.html")

    return app
