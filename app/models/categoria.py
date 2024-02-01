from app import db

class Categoria(db.Model):
    __tablename__ = 'Categoria'
    
    idCategoria = db.Column(db.Integer, primary_key=True)
    nombreCategoria = db.Column(db.String(255), nullable=False)
    