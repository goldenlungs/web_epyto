##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## api.py
##

from app import *
from app.models import *
from flask import *
import datetime 

class API(object):

    def __init__(self, app, connection):
        self.app = app
        slef.connection = connection
        self = User(app, connection)
        self.task = task(app, connection)

    def user_create(self, username, password):
        ret= {}
        if not username.isalnum():
            ret['ERROR'] = "internal error"
        else:
            if self.username.exist(username):
                ret['ERROR'] = "account already exist"
        else:
            
            if not username and not password:
                ret['ERROR'] = "internal error"

            else: 
                self.user.create(username, password)
                re['RESULT'] = "account  created"
        return json.dumps(ret)
    
    def user_login(self, username, password):
        ret = {}
        if not username and not password:
            ret['error'] = "login or paswword doesn't match"
        else: 
            if not self.user.exist(username):
                ret['error'] = "login or paswword doesn' march"
            elif not self.user.check_password(username, password):
                ret['error'] = "login or password doesn't match"
            else :
                session['username'] = username
                session['id'] = self.user.get_id(username)
                ret['result'] = "signin successful"
        return Json.dumps(ret)

    def user_logout(self):
        ret = {}
        session.pop('username', None)
        session.pop('id', None)
        ret['result'] = "signout successful"
        return Json.dumps(ret)



















