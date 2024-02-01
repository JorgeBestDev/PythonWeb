from app import db
from sqlalchemy import Column, Enum


PENDING ='PENDING'
COMPLETED = 'COMPLETED'

class Orden(db.Model):
    __tablename__ = 'orden'
    
    idOrden = db.Column(db.Integer,  primary_key=True)
    usuarioForaneo = db.Column(db.Integer,  db.ForeignKey('usuario.idUsuario'), nullable=False)
    precioOrden = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    status = Column(Enum(PENDING, COMPLETED, name='status_enum'), default=PENDING, nullable=False)
    pedido = db.relationship('Pedido', backref='orden', lazy='dynamic')
    
