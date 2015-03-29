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

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'