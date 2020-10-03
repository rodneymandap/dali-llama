from flask import Flask
from flask import render_template
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def about():
    return render_template('meet_the_team.html')