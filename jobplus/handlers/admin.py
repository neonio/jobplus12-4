from flask import Blueprint, render_template


admin: Blueprint = Blueprint('admin', __name__, url_prefix='/admin')
@admin.route('/')
def index():
    return "admin"
