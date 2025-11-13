from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import User
import random

# ------------------ AUTH ROUTES ------------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Welcome back, ' + user.username + '!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))


# ------------------ DASHBOARD ------------------

BIBLE_VERSES = [
    "Psalm 34:18 – The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
    "Isaiah 41:10 – Fear not, for I am with you; be not dismayed, for I am your God.",
    "Jeremiah 29:11 – For I know the plans I have for you, declares the Lord.",
    "Wisdom 3:9 – Those who trust in him will understand truth, and the faithful will abide with him in love.",
    "Sirach 2:10 – Consider the generations of old and see: has anyone trusted in the Lord and been disappointed?",
    "2 Maccabees 15:7 – Maccabeus never doubted that God would help him.",
    "Psalm 147:3 – He heals the brokenhearted and binds up their wounds.",
    "Tobit 13:2 – He afflicts and shows mercy; he brings down to Hades and raises up again.",
    "Baruch 5:1 – Take off your robe of mourning and misery; put on the splendor of glory from God forever.",
    "Lamentations 3:22–23 – The steadfast love of the Lord never ceases; his mercies never come to an end.",
]

SAINT_QUOTES = [
    "St. Augustine: Hope has two beautiful daughters – anger and courage.",
    "St. Francis of Assisi: Start by doing what's necessary; then do what's possible.",
    "St. Catherine of Siena: Be who God meant you to be and you will set the world on fire.",
    "St. Thérèse of Lisieux: The world’s thy ship, not thy home.",
    "St. Padre Pio: Pray, hope, and don’t worry.",
    "St. John Paul II: Do not be afraid. Open wide the doors for Christ.",
    "St. Teresa of Calcutta: If you can’t feed a hundred people, feed just one.",
    "St. Benedict: Prefer nothing whatever to Christ.",
    "St. Ignatius of Loyola: Go forth and set the world on fire.",
    "St. Josephine Bakhita: The Lord has loved me so much; we must love everyone.",
]

@app.route('/dashboard')
@login_required
def dashboard():
    random_verse = random.choice(BIBLE_VERSES)
    random_quote = random.choice(SAINT_QUOTES)
    return render_template('dashboard.html', verse=random_verse, quote=random_quote)
