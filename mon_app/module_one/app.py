from distutils.log import debug
from flask import Flask, render_template





app = Flask(__name__, template_folder = "templates")

@app.route('/')

def home():

    """the home page of our site"""

    return render_template('index.html')

