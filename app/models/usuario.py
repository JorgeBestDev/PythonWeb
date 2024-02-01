from app import db 

class Usuario(db.Model):
    __tablename__ = 'usuario'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nommbreUsuario = db.Column(db.String(255), nullable=False)
    correoUsuario = db.Column(db.String(255), nullable=False)
    contraseñaUsuario = db.Column(db.String(255), nullable=False)
    paymentMethodForaneo = db.Column(db.Integer, db.ForeignKey('Payment_method.idPayment_method'))
    orden = db.relationship('Orden', backref='usuario', lazy='dynamic')
