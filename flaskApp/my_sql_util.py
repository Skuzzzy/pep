from config import mysql

def get_tag_string_for_picture(picture_id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT Tags.tag_title FROM Tags INNER JOIN PictureTags ON Tags.tag_id=PictureTags.tag_id WHERE PictureTags.item_id="+picture_id+"")
    querylist = list(cursor.fetchall())
    tagstrings = []
    for each in querylist:
        tagstrings += [each[0]]
    return tagstrings

def getPicIDsFromTagID(tagID):
    conn = mysql.connect()
    cursor = conn.cursor()
    #cursor.execute("SELECT Tags.tag_title FROM Tags INNER JOIN PictureTags ON Tags.tag_id=PictureTags.tag_id")
    # SELECT item_id FROM PictureTags WHERE tag_id
    # join on tag_id select item_id where tag_title=tag
    querylist = list(cursor.fetchall())
    return -1
