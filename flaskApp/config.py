from flaskApp import app

### SQL CONFIG ###
from flaskext.mysql import MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '' # TODO Before putting this online put a sane password on the database
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
### END SQL CONFIG ###