from config import mysql
from config import UPLOAD_FOLDER


def get_tag_string_for_picture(picture_id):
    conn = mysql.connect()
    escaped_picture_id = conn.escape_string(str(picture_id))
    cursor = conn.cursor()
    cursor.execute("SELECT Tags.tag_title FROM Tags INNER JOIN PictureTags ON Tags.tag_id=PictureTags.tag_id WHERE PictureTags.item_id="+escaped_picture_id+"")
    query_list = list(cursor.fetchall())
    tag_strings = []
    for each in query_list:
        tag_strings += [each[0]]
    return tag_strings


def get_picture_table_information():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Pictures ORDER BY time_created DESC") # Currently showing the last uploaded picture as first
    link_list = list(cursor.fetchall())
    modified_links = []
    for each in link_list:
        modified_links.append([each[0], each[1], each[2], UPLOAD_FOLDER+each[3]]) # Todo change this to an image render route

    return modified_links


def get_last_n_pictures_created(n):
    conn = mysql.connect()
    cursor = conn.cursor()
    escaped_n = conn.escape_string(str(n))
    cursor.execute("SELECT * from Pictures ORDER BY time_created DESC LIMIT "+escaped_n+"")
    link_list = list(cursor.fetchall())
    modified_links = []
    for each in link_list:
        modified_links.append([each[0], each[1], each[2], UPLOAD_FOLDER+each[3]])
    return modified_links


def get_picture_from_id(picture_id):
    conn = mysql.connect()
    escaped_picture_id = conn.escape_string(str(picture_id))
    cursor = conn.cursor()
    cursor.execute("SELECT * from Pictures where id='" + escaped_picture_id + "'")
    data = cursor.fetchone()
    return data


def create_picture_entry_and_get_id(title,full_filename):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Pictures (time_created, title, file_name) VALUES (now(), '"+ title +"','"+ full_filename +"')")
    conn.commit()
    cursor.execute("SELECT id from Pictures where title='" + title + "' AND file_name='"+ full_filename + "'")
    current = cursor.fetchone()

    picture_id = current[0]
    return picture_id


def associate_picture_and_tag(picture_id, tag_id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO PictureTags (item_id, tag_id) VALUES ('" + str(picture_id)+"','" + str(tag_id) + "')")
    conn.commit()

def what(tag_list):

    conn = mysql.connect()
    cursor = conn.cursor()

    query = "SELECT Pictures.id, Pictures.time_created, Pictures.title, Pictures.file_name FROM Pictures INNER JOIN PictureTags ON Pictures.id=PictureTags.item_id INNER JOIN Tags ON PictureTags.tag_id=Tags.tag_id"
    append_string = ""

    if len(tag_list) > 0:
        append_string = " WHERE "

    for indx, val in enumerate(tag_list):
        if indx != 0:
            append_string += "OR "
        append_string += "Tags.tag_title='"+val.lower()+"' "

    append_string += " GROUP BY Pictures.id"

    print query + append_string
    cursor.execute(query + append_string)
    link_list = list(cursor.fetchall())
    modified_links = []
    for each in link_list:
        modified_links.append([each[0], each[1], each[2], UPLOAD_FOLDER+each[3]]) # Todo change this to an image render route

    return modified_links

'''
2 components
Joining the correct tables
THIS
SELECT * FROM Pictures INNER JOIN PictureTags ON Pictures.id=PictureTags.item_id INNER JOIN Tags ON PictureTags.tag_id=Tags.tag_id
COMPLETE

Building the WHERE clause
TODO
'''
