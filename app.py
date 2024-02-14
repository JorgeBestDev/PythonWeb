from flask import Flask, render_template,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Enum
from flask_login import LoginManager
from app import create_app,db
from datetime import timedelta
import os
import secrets
import string

def generate_secret_key(length=32):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

secret_key = generate_secret_key()

app = create_app()
app.config['SECRET_KEY'] = 'claveSecreta'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)


@app.route('/')
def index():
    username = session.get('username')
    return render_template('index.html', username=username)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))