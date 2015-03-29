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
        cursor.execute("insert into Pair values ('','" + request.form['name'] + "','" + request.form['link'] + "')")
        conn.commit()
        return redirect('/')
    else:
        return render_template('addlink.html')

@app.route('/list')
def listLinks():

    cursor = mysql.connect().cursor()
    result = cursor.execute("SELECT * from Pair")

    list = []

    return render_template('list.html', list=list)

@app.route('/test')
def test():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Pair")
    data = cursor.fetchone()
    print data
    return "", 1
