from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("index.html")


   
