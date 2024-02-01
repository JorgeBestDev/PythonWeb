from app import db 

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nommbreUsuario = db.Column(db.String(255), nullable=False)
    correoUsuario = db.Column(db.String(255), nullable=False)
    contraseñaUsuario = db.Column(db.String(255), nullable=False)
    paymentMethodForaneo = db.Column(db.Integer, db.ForeignKey('Payment_methods.idPayment_methods'))
