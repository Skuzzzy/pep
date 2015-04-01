import os, datetime

def save_file_and_get_name(ul_file):
    now_str = str(datetime.datetime.now().time())
    file_extension = ul_file.filename.split(".")[-1]
    full_filename = now_str + '.' + file_extension
    save_file = os.path.dirname(os.path.realpath(__file__)) + '/static/frogpic/' + full_filename
    ul_file.save(save_file)
    return full_filename
