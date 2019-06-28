from flask import Blueprint, render_template


job: Blueprint = Blueprint('job', __name__, url_prefix='/job')
@job.route('/')
def index():
    return "job"
