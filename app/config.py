import os
import secrets
from datetime import timedelta
#kqra jnuo zayw sixi
SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(32))
PERMANENT_SESSION_LIFETIME = timedelta(days=365)

#credenciales base de datos db4free.net
#nombre base de datos: proyecto_python
#Nombre de usuario MySQL: admin34587209
#Contraseña de usuario MySQL:@Bh!5H2$9Lqz&7pX
#correo administrador web: administrador@tiendaonline.com
#contraseña administrador web: W#u8@r!P5b2$qF9Z
#contraseña hasheada scrypt:32768:8:1$l3kNvbbSLHpnZDZe$192ee8d615806f7217a2101b7c752579e2a4fc0d2032075e8b0baa1fca07b60a63b175bf80c74b9ae0738fdbb0524f2e8fc3aec6224d92d760dc17c2c804ff94
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sql5685117:lLtKytF3AK@sql5.freemysqlhosting.net:3306/sql5685117'
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'pruebaemailsconfirmacion@gmail.com')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'kqrajnuozaywsixi')

