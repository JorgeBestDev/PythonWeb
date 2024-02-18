from flask_login import (
    login_required,
    login_manager,
    UserMixin,
    login_user,
    logout_user,
    current_user,
)
from flask import Blueprint, render_template, flash, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models.usuario import Usuario
from app.models.administrador import Administrador
from app.models.pais import Pais
from sqlalchemy.exc import IntegrityError



bp = Blueprint("administrador", __name__)

@bp.route('/administrador')
def index():
    return render_template('administrador/index.html', user=current_user)


