from flaskApp import app

@app.route('/')
@app.route('/index')
def index():
    return "chips!"