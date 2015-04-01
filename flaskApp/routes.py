from flaskApp import app

from config import mysql

import my_sql_util

from flask import render_template
from flask import request, redirect, send_file

import file_util

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/list')
def list_links():
    modified_links = my_sql_util.get_picture_table_information()
    for each in modified_links:
        each.append(my_sql_util.get_tag_string_for_picture(each[0])) # each[0] is the picture_id
    return render_template('list.html', list=modified_links)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        ul_file = request.files['frogpic']

        full_filename = file_util.save_file_and_get_name(ul_file)
        # Insert into pictures
        picture_id = my_sql_util.create_picture_entry_and_get_id(request.form['name'],full_filename)

        # Associate tags
        tag_tokens = request.form['tags'].split(",") # Get tags from post

        conn = mysql.connect()
        cursor = conn.cursor()

        tag_ids = []
        for tag in tag_tokens:
            low_tag = tag.lower()
            cursor.execute("SELECT tag_id from Tags where tag_title='" + low_tag + "'")
            tagInDB = cursor.fetchone()
            if cursor.rowcount == 0: # If this tag doesn't exist in the database insert it
                cursor.execute("INSERT INTO Tags (tag_title) VALUES ('"+ str(low_tag) +"')")
                cursor.execute("SELECT tag_id from Tags where tag_title='" + low_tag + "'")
                tagInDB = cursor.fetchone()
            tag_ids.append(tagInDB)

        for tag_id in tag_ids:
            my_sql_util.associate_picture_and_tag(picture_id,tag_id[0])

        conn.commit()
        return redirect('/')
    else:
        return render_template('fileupload.html')

@app.route('/image/<picture_id>')
def picture(picture_id):
    data = my_sql_util.get_picture_from_id(picture_id)
    if data is None:
        return redirect('/')
    else:
        filename = data[3]
        return send_file("static/frogpic/"+filename, mimetype='image/gif')


