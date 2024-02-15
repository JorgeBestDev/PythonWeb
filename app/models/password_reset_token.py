from app import db 
from flask_login import UserMixin
from datetime import datetime, timedelta

class PasswordResetToken(db.Model, UserMixin):
    __tablename__ ='password_reset_token'
    idPRT = db.Column(db.Integer, primary_key=True)
    idUsuarioForaneo = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'), nullable=False)
    token = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)    