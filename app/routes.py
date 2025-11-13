from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def home():
    return "<h1>Welcome to the Catholic Hospital Chaplaincy System</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        # For now, just redirect to home
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        # For now, just redirect to login
        return redirect(url_for('login'))
    return render_template('register.html')
