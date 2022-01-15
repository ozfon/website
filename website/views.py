from re import I
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/index')
def home():
    return render_template('index.html')

@views.route('/projects')
def projects():
    return render_template('projects.html')

@views.route('/tools')
def tools():
    return render_template('tools.html')