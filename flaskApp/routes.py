from flaskApp import app

from config import mysql

from flask import render_template
from flask import request, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/addlink', methods=['GET', 'POST'])
def addlink():
    if request.method == 'POST':
        conn = mysql.connect()
        cursor = conn.cursor()
        conn.commit()
        return redirect('/')
    else:
        return render_template('addlink.html')

@app.route('/test')
def test():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User")
    data = cursor.fetchone()
    print data
    return "", 1
