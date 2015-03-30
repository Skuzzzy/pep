from flaskApp import app

from config import mysql

from flask import render_template
from flask import request, redirect

import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/addlink', methods=['GET', 'POST'])
def addlink():
    if request.method == 'POST':
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("insert into Pictures values ('',now(),'" + request.form['name'] + "','" + request.form['link'] + "')")
        conn.commit()
        return redirect('/')
    else:
        return render_template('addlink.html')

@app.route('/list')
def listLinks():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Pictures")
    linklist = list(cursor.fetchall())
    return render_template('list.html', list=linklist)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        ul_file = request.files['frogpic']

        save_file = 'frogpic/' + str(datetime.datetime.now().time()) + '.jpg'
        ul_file.save(save_file)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("insert into Pictures values ('',now(),'" + request.form['name'] + "','" + save_file + "')")
        conn.commit()
        return redirect('/')
    else:
        return render_template('fileupload.html')
