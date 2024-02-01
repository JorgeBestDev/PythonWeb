from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Enum
from app import create_app,db
import os

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))