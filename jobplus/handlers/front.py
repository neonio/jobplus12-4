from flask import Blueprint, render_template


front: Blueprint = Blueprint('front', __name__, url_prefix='/front')
@front.route('/')
def index():
    return "front"
