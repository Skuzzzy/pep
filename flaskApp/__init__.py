from flask import Flask

app = Flask(__name__)

### SQL CONFIG ###
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '' # TODO Before putting this online put a sane password on the database
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
### END SQL CONFIG ###

from flaskApp import routes