from flask import Blueprint, render_template

tools = Blueprint('tools', __name__)

@tools.route('quad_calc')
def quad_calc():
    return render_template('tools/quad_calc.html')