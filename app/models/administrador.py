from app import db 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Administrador(db.Model, UserMixin):
    __tablename__ = 'administrador'
    idAdministrador = db.Column(db.Integer, primary_key=True)
    correoAdministrador = db.Column(db.String(255), nullable=False)
    contraseñaAdministrador = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<Usuario {self.correoAdministrador}>'

    def is_authenticated(self):
        return True  # Siempre devolvemos True porque todos los usuarios autenticados son válidos

    def is_active(self):
        return True  # Aquí puedes implementar lógica para desactivar cuentas de usuario si es necesario

    def is_anonymous(self):
        return False  # Devolvemos False porque los usuarios autenticados no son anónimos

    def get_id(self):
        return str(self.idAdministrador)  # Devolvemos el ID del usuario como una cadena Unicode
    
    def set_password(self, password):
        self.correoAdministrador = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contraseñaAdministrador, password)