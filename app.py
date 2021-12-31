from flask import Flask
import sys
app = Flask(__name__)

@app.route('/Test')
def Hello_World():
    msg = sys.executable
    return msg