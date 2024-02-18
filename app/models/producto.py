from app import db

class Producto(db.Model):
    __tablename__ = 'producto'
    idProducto = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(255), nullable=False, index=True)
    precioProducto = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    nombreImagen = db.Column(db.String(4096), nullable=False)  # Ruta de la imagen del producto
    pedido = db.relationship('Pedido', backref='producto', lazy='dynamic')
    
