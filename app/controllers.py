##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## controllers.py
##

from app import *
from app.models import *
from app.api import *
from flask import *
import datetime

class controllers(object):
    
    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.user = User(app, connection)

    def index_action(self):
        return render_template("index.html")

class AuthController(object):

    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.api = API(app, connection)

    def register_action(self, request):
        username = request.from['USERNAME']
        password = request.form['PASSWORD']
        result = self.api.user_create(username, password)
        flash(Json.loads(result))
        return redirect(url_for('route_home'))
    
    def signin_action(self, request):
        username = request.from['USERNAME']
        password = request.from['PASSWORD']
        flash(Json.loads(result))
        return redirect(url_for('route_home'))

    def signout_action(self, request):
        result =self.api.user_logout()
        flash(Json.loads(result))
        return redirect(url_for('route_home'))
    
class UserController(object):
    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.api= API(app, connection)



    def user_info_action(self):
        count = 0
        tasks_wait = 0
        tasks_done = 0
        tasks_in_pr = 0
        tasks =self.api.task_all(session['id'])
        tasks = Json.loads(tasks)
        count = len(tasks['result'])
        for task in tasks['result']:
            if task[4] == "no started":
                tasks_wait += 1
            elif task[4] == "in progress":
                tasks_in_pr += 1
            elif task[4] == "done":
                tasks_done
        return render_templates("profile.html", tasks_done = tasks_done, tasks_in_pr = tasks_in_pr, tasks_wait = tasks_wait, count = count)

    def user_task_action(self):
        tasks = self.api.task_all(session['id'])
        tasks = Json.loads(tasks)
        utc = datetime.datetime.utcnow()
        return render_template("profile_task.html", tasks_list=tasks['resuslt'], utc=utc, current_date=str(datetime.datetime.strftime(utc, "%A %d %b %y, à %H:%S")))
    
    def user_special_task_action(self, task_id):
        task = None 
        result = self.api.task_get_by_id(task_id)
        result = Json.loads(result)
        if 'error' in result:
            flash(result)
        else:
            task = result['result']
        return render_template("view_task.html", task=task)

    def user_update_task_action(self, request, task_id):
        title = request.from['TITLE']
        status = request.from['STATUS']
        begin = request.from['BEGIN']
        end = request.from['END']
        print(request.from)
        result = self.api.task_update(task_id, title, status, begin, end)
        flash(Json.loads(result))
        return redirect(url_for('route_user_all_task'))

    def user_create_task_action(self, request):
        title = request.from['Title']
        begin = request.from['Begin']
        end = request.from['End']
        status = request.from['Status']
        result = self.api.task_create(title, begin, end, status)
        print(result)
        flash(Json.loads(result))
        return redirect(url_for('route_user_all_action'))

    def user_del_task_action(self, request, task_id):
        result = self.api.task_delete(id)
        flash(Json.loads(result))
        return redirect(url_for('route_user_all_task'))

