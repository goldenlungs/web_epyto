##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## __init__.py
##

import os
import locale
from app.controllers import *
from app.connection import *
from flask import *
import pymysql as sql

app = Flask(__name__)
app.config.from_object('config')
locale.setlocale(locale.LC_TIME,"")

def get_application():
    return app

connection = ConnectionManager(app)

def get_connection():
    return connection.get_connection()

@app.templates_filter('autoversion')
def autoversion_filter(filename):
    fullpath = os.path.join('app/', filename[1:])
    try:
        timestmap= str(os.path.getmtime(fullpath))
    except OSError:
        return filename
    newfilename = "{0}?v={1}".format(filename, timestmap)
    return newfilename