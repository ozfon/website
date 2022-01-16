from flask import Blueprint, render_template, request, flash
import os

if os.uname()[4][:3] == 'arm':
    led = 18
    import RPi.GPIO as GPIO

tools = Blueprint('tools', __name__)

@tools.route('quad_calc')
def quad_calc():
    return render_template('tools/quad_calc.html')

@tools.route('led_control', methods=["POST", "GET"])
def led_control():
    if os.uname()[4][:3] == 'arm':
        if request.method == 'POST':
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
