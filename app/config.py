import os
import secrets
from datetime import timedelta
#kqra jnuo zayw sixi
SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(32))
PERMANENT_SESSION_LIFETIME = timedelta(days=365)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:BeDdh5AEHg23fGbEGca4-Dbb3ch6DC2e@viaduct.proxy.rlwy.net:15114/proyecto_formativo'
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'pruebaemailsconfirmacion@gmail.com')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'kqrajnuozaywsixi')

