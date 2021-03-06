from flaskApp import app

### SQL CONFIG ###
from flaskext.mysql import MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '' # TODO Before putting this online put a sane password on the database
app.config['MYSQL_DATABASE_DB'] = 'pepdb'
mysql.init_app(app)
### END SQL CONFIG ###


# TODO Actually use these configs
UPLOAD_FOLDER = "../static/frogpic/"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])