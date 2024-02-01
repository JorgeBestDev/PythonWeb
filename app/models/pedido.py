from app import db


class Pedido(db.Model):
    __tablename__ = 'pedidos'
    idPedido = db.Column(db.Integer,  primary_key=True)
    ordenForaneo = db.Column(db.Integer,  db.ForeignKey('orden.idOrden'), nullable=False)
    productoForaneo = db.Column(db.Integer,  db.ForeignKey('producto.idProducto'), nullable=False)
    cantidadPedido = db.Column(db.Integer, nullable=False, default=1)
    totalPedido = db.Column(db.Numeric(precision=10, scale=2), nullable=False)