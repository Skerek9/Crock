
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

#Конфигурация
DATABASE = '/tmp/crck.db'
DEBUG = True
SECRET_KEY = 'gfvcxczdxssrfgyhuji'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE = os.path.join(app.root_path, 'Crock.db')))

def connect_db():
    conn = sqlite3.connect('Crock.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode = 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

create_db()

@app.route("/", methods = ['GET','POST'])
def nickname_page():
    return render_template('main.html')

@app.route("/lobby", methods = ['GET','POST'])
def lobby():
    if request.method == 'POST':
        print(request.form)
    return render_template('lobby.html')

@app.route("/results")
def results():
    return render_template('results.html')

@app.route("/game")
def game():
    return render_template('game.html')

@app.route("/search")
def search():
    return render_template('search.html')

'''if __name__ == "__main__":
    app.run(debug = True)
'''

