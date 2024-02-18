from app import db


class Pedido(db.Model):
    __tablename__ = 'pedido'
    idPedido = db.Column(db.Integer,  primary_key=True)
    productoForaneo = db.Column(db.Integer, db.ForeignKey('producto.idProducto'), nullable=False)
    ordenes = db.relationship("Orden", back_populates="pedido")
    cantidadPedido = db.Column(db.Integer, nullable=False, default=1)
    totalPedido = db.Column(db.Numeric(precision=10, scale=2), nullable=False)