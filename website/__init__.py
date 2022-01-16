from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'peanut125butter'

    from .views import views
    from .auth import auth
    from .tools import tools

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(tools, url_prefix='/tools')

    return app

def IO_config():
    if os.uname()[4][:3] == 'arm':
        print("raspberry pi")
        import RPi.GPIO as GPIO

        led = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)
    elif os.uname()[4][:3] == 'x86':
        print("mac")
