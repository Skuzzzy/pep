from flask import Flask
from flaskext.mysql import MySQL


### SQL CONFIG ###
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '' # TODO Before putting this online put a sane password on the database
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
### END SQL CONFIG ###

### ROUTES ###
from flask import request

@app.route("/")
def hello():
    return "chips!"

### END ROUTES ###


if __name__ == "__main__":
    app.run()