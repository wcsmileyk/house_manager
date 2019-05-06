from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, errors, houses, inventory, projects, users