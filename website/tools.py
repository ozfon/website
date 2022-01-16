from flask import Blueprint, render_template
from flask.wrappers import Request
from werkzeug.wrappers import request
import os

if os.uname()[4][:3] == 'arm':
    from website import led, GPIO

tools = Blueprint('tools', __name__)

@tools.route('quad_calc')
def quad_calc():
    return render_template('tools/quad_calc.html')

@tools.route('led_control', methods=["POST", "GET"])
def led_control():
    if os.uname()[4][:3] == 'arm':
        if Request.method == 'POST':
            if request.form['submit_button'] == 'Off':
                GPIO.output(led, GPIO.HIGH)
                newName = 'On'
            elif request.form['submit_button'] == 'On':
                GPIO.output(led, GPIO.LOW)
                newName = 'Off'
        else:
            GPIO.output(led, GPIO.LOW)
            newName = 'Off'
    else:
        newName = 'Offline'
    return render_template('tools/led_controls.html', led_state = newName)