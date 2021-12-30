from flask import Flask
app = Flask(__name__)

@app.route('/tools/flask_app')
def Hello_World():
    return "Hello Flask!"