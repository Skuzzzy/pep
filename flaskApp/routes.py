from flaskApp import app

from config import mysql

from flask import render_template
from flask import request, redirect, send_file

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

    modifiedLinks = []
    for each in linklist:
        modifiedLinks.append([each[0], each[1], each[2], "../static/frogpic/"+each[3]])
    print modifiedLinks

    return render_template('list.html', list=modifiedLinks)


import os
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        ul_file = request.files['frogpic']

        nowstr = str(datetime.datetime.now().time())
        fileExtension = ul_file.filename.split(".")[-1]
        save_file = os.path.dirname(os.path.realpath(__file__)) + '/static/frogpic/' + nowstr + '.' + fileExtension
        ul_file.save(save_file)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("insert into Pictures values ('',now(),'" + request.form['name'] + "','" + nowstr + '.' + fileExtension + "')")
        conn.commit()
        return redirect('/')
    else:
        return render_template('fileupload.html')


@app.route('/test')
def test():
    return send_file("static/test.jpg", mimetype='image/gif')