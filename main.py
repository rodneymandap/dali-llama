import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__) 
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('meet_the_team.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/environment')
def environment():
    return render_template('environment.html')

@app.route('/insight')
def insight():
    return render_template('insights.html')

@app.route('/methodology')
def methodology():
    return render_template('methodology.html')

@app.route('/economics')
def economic():
    return render_template('socio_economics.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)