from app import db

class Producto(db.Model):
    __tablename__ = 'producto'
    idProducto = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(255), nullable=False, index=True)
    precioProducto = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    pedido = db.relationship('Pedido', backref='producto', lazy='dynamic')
