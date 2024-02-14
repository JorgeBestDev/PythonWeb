from app import db 

class Usuario(db.Model):
    __tablename__ = 'usuario'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(255), nullable=False)
    correoUsuario = db.Column(db.String(255), nullable=False)
    contraseñaUsuario = db.Column(db.String(255), nullable=False)
    paymentMethodForaneo = db.Column(db.Integer, db.ForeignKey('Payment_method.idPayment_method'))
    orden = db.relationship('Orden', backref='usuario', lazy='dynamic')
    
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.idPais'), nullable=False)  # Cambio de nombre a 'pais_id'
    
    direccion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(255), nullable=False)
    ciudad = db.Column(db.String(255), nullable=False)
    codigoPostal = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.correoUsuario}>'



