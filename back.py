from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import time

app = Flask(__name__)
app.secret_key = 'bossofthegym'

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client.HW2
users = db.users

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({"username": username})
        if user and user['password'] == password:
            session['user'] = username
            return redirect(url_for('redirect_to_profile'))
        else:
            return "Invalid credentials!", 401
    
    return render_template("login.html")

@app.route('/redirect')
def redirect_to_profile():
    if 'user' in session:
        return render_template('redirect.html', username=session['user'])
    return redirect(url_for('login'))
@app.route('/profile')
def profile():
    if 'user' in session:
        return render_template('profile.html', username=session['user'])
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)