from flask import Blueprint

myblueprint = Blueprint('myblueprint', __name__,
                        template_folder='templates')

@myblueprint.route('/')
def home():
    return "Hello, World!"