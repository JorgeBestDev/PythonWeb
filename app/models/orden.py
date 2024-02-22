from app import db
from sqlalchemy import Column, Enum
from sqlalchemy.orm import relationship


PENDING ='PENDING'
COMPLETED = 'COMPLETED'
DECLINED = 'DECLINED'

class Orden(db.Model):
    __tablename__ = 'orden'
    
    idOrden = db.Column(db.Integer, primary_key=True)
    precioOrden = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    status = db.Column(Enum(PENDING, COMPLETED, DECLINED, name='status_enum'), default=PENDING, nullable=False)
    
    carritoForaneo = db.Column(db.Integer, db.ForeignKey('carrito.idCarrito'), nullable=False)
    
