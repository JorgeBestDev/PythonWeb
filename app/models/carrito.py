from app import db


class Carrito(db.Model):
    __tablename__ = 'carrito'
    idCarrito = db.Column(db.Integer, primary_key=True)
    pedidoForaneo = db.Column(db.Integer, db.ForeignKey('pedido.idPedido', ondelete='CASCADE'),nullable=False)
    
    