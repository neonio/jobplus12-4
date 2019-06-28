from flask import Blueprint
from .front import front
from .admin import admin
from .company import company
from .job import job
from .user import user

blueprints: [Blueprint] = [front, admin, company, job, user]
