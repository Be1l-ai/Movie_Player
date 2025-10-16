from flask import Blueprint

movie_bp = Blueprint('movie', __name__)

from . import movie_route