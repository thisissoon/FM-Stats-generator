from flask import Blueprint

route = Blueprint('api', __name__)

from app.api.v1 import views
