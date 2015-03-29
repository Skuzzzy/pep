from flaskApp import app
from config import mysql

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User")
    data = cursor.fetchone()
    print data
    return "", 1
