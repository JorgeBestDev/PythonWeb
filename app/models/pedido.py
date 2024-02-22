from app import db


class Pedido(db.Model):
    __tablename__ = 'pedido'
    idPedido = db.Column(db.Integer,  primary_key=True)
    productoForaneo = db.Column(db.Integer, db.ForeignKey('producto.idProducto'), nullable=False)
    usuarioForeaneo = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'), nullable=False)
    cantidadPedido = db.Column(db.Integer, nullable=False, default=1)
    totalPedido = db.Column(db.Numeric(precision=10, scale=2), nullable=False)