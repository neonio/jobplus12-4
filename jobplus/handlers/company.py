from flask import Blueprint, render_template


company: Blueprint = Blueprint('company', __name__, url_prefix='/company')
@company.route('/')
def index():
    return "company"

@company.route('/admin_index/')
def admin_index():
    return "admin_index"
