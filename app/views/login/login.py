from flask import Flask, render_template, request, redirect, url_for, session
from models import User

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route('/')
def home():
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.authenticate(email, password)
        if user:
            session['user'] = user.email
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid email or password')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))