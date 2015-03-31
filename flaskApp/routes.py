from flaskApp import app

from config import mysql

from flask import render_template
from flask import request, redirect, send_file

import datetime
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/list')
def listLinks():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Pictures")
    linklist = list(cursor.fetchall())

    modifiedLinks = []
    for each in linklist:
        modifiedLinks.append([each[0], each[1], each[2], "../static/frogpic/"+each[3]])

    return render_template('list.html', list=modifiedLinks)



@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        ul_file = request.files['frogpic']

        nowstr = str(datetime.datetime.now().time())
        fileExtension = ul_file.filename.split(".")[-1]
        save_file = os.path.dirname(os.path.realpath(__file__)) + '/static/frogpic/' + nowstr + '.' + fileExtension
        ul_file.save(save_file)

        # Insert into pictures
        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Pictures (time_created, title, file_name) VALUES (now(), '"+ request.form['name'] +"','"+ nowstr + '.' + fileExtension +"')")

        cursor.execute("SELECT id from Pictures where title='" + request.form['name'] + "' AND file_name='"+ nowstr + '.' + fileExtension + "'")
        current = cursor.fetchone()
        picture_id = current[0]

        # Associate tags
        tagtokens = request.form['tags'].split(",") # Get tags from post

        tag_ids = []
        for tag in tagtokens:
            low_tag = tag.lower()
            cursor.execute("SELECT tag_id from Tags where tag_title='" + low_tag + "'")
            tagInDB = cursor.fetchone()
            if cursor.rowcount == 0: # If this tag doesn't exist in the database insert it
                cursor.execute("INSERT INTO Tags (tag_title) VALUES ('"+ str(low_tag) +"')")
                cursor.execute("SELECT tag_id from Tags where tag_title='" + low_tag + "'")
                tagInDB = cursor.fetchone()
            tag_ids.append(tagInDB)

        for tag_id in tag_ids:
            cursor.execute("INSERT INTO PictureTags (item_id, tag_id) VALUES ('" + str(picture_id)+"','" + str(tag_id[0]) + "')")

        conn.commit()
        return redirect('/')
    else:
        return render_template('fileupload.html')

@app.route('/image/<ID>')
def picture(ID):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from Pictures where id='" + ID + "'")
    data = cursor.fetchone()
    if data is None:
        return redirect('/')
    else:
        filename = data[3]
        return send_file("static/frogpic/"+filename, mimetype='image/gif')



