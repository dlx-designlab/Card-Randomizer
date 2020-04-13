from flask import Blueprint

js = Blueprint("javascript", __name__, static_url_path='/javascript', static_folder='./static/javascript')
css = Blueprint("css", __name__, static_url_path='/css', static_folder='./static/css')
image = Blueprint("image", __name__, static_url_path='/image', static_folder='./static/image')