from app import db 

class Usuario_has_Orden(db.Model):
    __tablename__ = 'usuario_has_orden'
    usuarioForaneo = db.Column(db.Integer,  db.ForeignKey('usuario.idUsuario'), primary_key=True)
    ordenForaneo = db.Column(db.Integer,  db.ForeignKey('orden.idOrden'), primary_key=True)
    