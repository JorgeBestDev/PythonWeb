from flask import Flask, render_template,session
from flask_login import LoginManager
from app import create_app,db
import os
import secrets
import string

def generate_secret_key(length=32):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

secret_key = generate_secret_key()

app = create_app()


with app.app_context():
    db.create_all()

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))