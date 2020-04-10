##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## views.py
##

from app import *

##index route
@app.route('/', methods = ['GET'])
@app.route ('/ index', methods = ['GET'])
def route_home():
    controller = controller(app, get_connection())
    return "Hello world !\n"
    return controller.index_action()

@app.route('/register', methods = ['POST'])
def route_register():
    controller = AuthController(app, get_connection())
    return controller.register_action(request)

@app.route('/signin', methods = ['POST'])
def route_signin():
    controller = AuthController(app, get_connection())
    return controller.signin_action(request)

@app.route('/signout', methods = ['POST'])
def route_signout():
    controller = AuthController(app, get_connection())
    return controller.signout_action(request)

@app.route('/user', methods = ['GET'])
def route_user_info():
    controller = UserController(app, get_connection())
    return controller.user_info_action()

@app.route('/user/task', methods = ['GET'])
def route_user_task():
    controller = UserController(app, get_connection())
    return controller.user_task_action()

@app.route('user/task/<int:task_id>', methods = ['GET'])
def route_user_special_task(task_id):
    controller = UserController(app, get_connection())
    return controller.user_special_task_action(task_id)

@app.route('user/task/<int:task_id>' methods = ['POST'])
def route_user_update_task(task_id):
    controller = UserController(app, get_connection())
    return controller.user_update_task_action(request, id)

@app.route('/user/task/add', methods = ['POST'])
def route_user_create_task():
    controller = UserController(app, get())
    return controller.user_create_task_action(request)

@app.route('/user/task/del/<int:task_id>', methods = ['POST'])
def route_user_del_task(task_id):
    controller = UserController(app, get_connection())
    return controller.user_del_task_action(request, task_id)
