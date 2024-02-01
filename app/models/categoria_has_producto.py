from app import db 

class Categoria_has_producto(db.Model):
    __tablename__ = 'Categoria_has_Producto'
    categoriaForaneo = db.Column(db.Integer,  db.ForeignKey('categoria.idCategoria'), primary_key=True)
    productoForaneo = db.Column(db.Integer,  db.ForeignKey('producto.idProducto'), primary_key=True)