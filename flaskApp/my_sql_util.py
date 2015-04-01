from config import mysql

def get_tag_string_for_picture(picture_id):
    conn = mysql.connect()
    escaped_picture_id = conn.escape_string(str(picture_id))
    cursor = conn.cursor()
    cursor.execute("SELECT Tags.tag_title FROM Tags INNER JOIN PictureTags ON Tags.tag_id=PictureTags.tag_id WHERE PictureTags.item_id="+escaped_picture_id+"")
    querylist = list(cursor.fetchall())
    tagstrings = []
    for each in querylist:
        tagstrings += [each[0]]
    return tagstrings

def get_picture_table_information():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Pictures")
    link_list = list(cursor.fetchall())
    modified_links = []
    for each in link_list:
        modified_links.append([each[0], each[1], each[2], "../static/frogpic/"+each[3]])
    return modified_links

def get_last_n_pictures_created(n):
    conn = mysql.connect()
    cursor = conn.cursor()
    escaped_n = conn.escape_string(str(n))
    cursor.execute("SELECT * from Pictures ORDER BY time_created DESC LIMIT "+escaped_n+"")
    link_list = list(cursor.fetchall())
    modified_links = []
    for each in link_list:
        modified_links.append([each[0], each[1], each[2], "../static/frogpic/"+each[3]])
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

def get_picture_ids_associated_with_tag(tag_id):
    conn = mysql.connect()
    cursor = conn.cursor()
    #cursor.execute("SELECT Tags.tag_title FROM Tags INNER JOIN PictureTags ON Tags.tag_id=PictureTags.tag_id")
    # SELECT item_id FROM PictureTags WHERE tag_id
    # join on tag_id select item_id where tag_title=tag
    querylist = list(cursor.fetchall())
    return -1
