from flask import Blueprint, render_template


front: Blueprint = Blueprint('front', __name__, url_prefix='/front')
@front.route('/')
def index():
    return "front"


@front.route('/userregister/')
def userregister():
    return "userregister"


@front.route('/companyregister/')
def companyregister():
    return "companyregister"

@front.route('/login/')
def login():
    return "login"

@front.route('/logout/')
def logout():
    return "logout"
