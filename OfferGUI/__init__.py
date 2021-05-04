from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from werkzeug.utils import secure_filename
app = Flask(__name__)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Costs.db'
app.config['SECRET_KEY'] = '859e01ebc245b0ae49600efa'
app.config['UPLOAD_PATH'] = 'uploads'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from OfferGUI import routes


