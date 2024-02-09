from app import db

class Pais(db.Model):
    __tablename__ = 'pais'
    idPais = db.Column(db.Integer, primary_key=True)
    nombrePais = db.Column(db.String(255), nullable=False)
    usuario = db.relationship('Usuario', backref='pais', lazy='dynamic')
