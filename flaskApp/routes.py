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

@app.route('/list')
def listLinks():
    list = [
        {'name': "Southpark", 'link': "http://i.imgur.com/0Ux0Mqt.jpg"}
    ]
    return render_template('list.html', list=list)

@app.route('/test')
def test():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User")
    data = cursor.fetchone()
    print data
    return "", 1
