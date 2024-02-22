from app import db


class Carrito(db.Model):
    __tablename__ = 'carrito'
    idCarrito = db.Column(db.Integer, primary_key=True)
    idPedido = db.Column(db.Integer, db.ForeignKey('pedido.idPedido'),nullable=False)
    
    