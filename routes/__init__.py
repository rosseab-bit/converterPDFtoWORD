from flask import Blueprint
routes = Blueprint('routes', __name__)

# importo las rutas.
from .index import *
from .upload import *
