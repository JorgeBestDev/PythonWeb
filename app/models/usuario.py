from app import db 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(255), nullable=False)
    correoUsuario = db.Column(db.String(255), nullable=False)
    contraseñaUsuario = db.Column(db.String(255), nullable=False)
    telefonoUsuario = db.Column(db.BigInteger, unique=True)
    paymentMethodForaneo = db.Column(db.Integer, db.ForeignKey('Payment_method.idPayment_method'))
    
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.idPais'), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(255), nullable=False)
    ciudad = db.Column(db.String(255), nullable=False)
    codigoPostal = db.Column(db.Integer, nullable=False)
    password_reset_tokens = db.relationship("PasswordResetToken", backref="usuario", lazy='dynamic')
    es_administrador = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Usuario {self.correoUsuario}>'

    def is_authenticated(self):
        return True  # Siempre devolvemos True porque todos los usuarios autenticados son válidos

    def is_active(self):
        return True  # Aquí puedes implementar lógica para desactivar cuentas de usuario si es necesario

    def is_anonymous(self):
        return False  # Devolvemos False porque los usuarios autenticados no son anónimos

    def get_id(self):
        return str(self.idUsuario)  # Devolvemos el ID del usuario como una cadena Unicode
    
    def set_password(self, password):
        self.contraseñaUsuario = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contraseñaUsuario, password)
