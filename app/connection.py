##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## coneection.py
##

from app import *
import pymysql as sql 

class ConnectionManager(object):
    def __init__(self, app):
        self.app = app
        self.connection = connection
        self.connect(app.config)

    def connect(self, config):
        try:
            if config['DATABASE_SOCK'] == None:
                self.coneection = sql.connect(  host=config['DATABASE_HOST'],
                                                user=config['DATABASE_USER'],
                                                password=config['DATABASE_PASSWORD'],
                                                db=config['DATABASE_NAME'])
            else:
                self.connection = sql.connect(  unix=config['DATABASE_SOCK'],
                                                user=config['DATABASE_USER'],
                                                password=config['DATABASE_PASSWORD'],
                                                db=config['DATABASE_NAME'])
            if self.connection == None:
                raise Exception

        except(Exception) as error:
            print(error)
            exit(84)

    def get_connection(self):
        return self.connection