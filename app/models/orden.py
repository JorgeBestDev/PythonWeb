from app import db
from sqlalchemy import Column, Enum
from sqlalchemy.orm import relationship


PENDING ='PENDING'
COMPLETED = 'COMPLETED'
DECLINED = 'DECLINED'

class Orden(db.Model):
    __tablename__ = 'orden'
    
    idOrden = db.Column(db.Integer,  primary_key=True)
    precioOrden = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    usuarios = db.relationship("Usuario", secondary="usuario_has_orden", back_populates="ordenes")
    status = Column(Enum(PENDING, COMPLETED, DECLINED, name='status_enum'), default=PENDING, nullable=False)
    
    pedidoForaneo = db.Column(db.Integer, db.ForeignKey('pedido.idPedido'), nullable=False)
    pedido = db.relationship("Pedido", back_populates="ordenes")
    
