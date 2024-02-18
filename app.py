from app import create_app,db
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
import os
from datetime import datetime, timedelta
from hashlib import sha256
from flask import request, render_template, redirect, url_for, flash
from flask_login import (
    login_required,
    login_manager,
    UserMixin,
    login_user,
    logout_user,
    current_user,
)
from flask_mail import Message,Mail
from app.models.usuario import Usuario
from app.models.password_reset_token import PasswordResetToken
from werkzeug.security import check_password_hash, generate_password_hash

app = create_app()
mail = Mail(app)


def generate_token(email):
    # Genera un token único basado en el correo electrónico del usuario y la fecha actual
    token_data = f"{email}{datetime.now()}"
    return sha256(token_data.encode()).hexdigest()

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password_request():
    logout_user()
    if request.method == 'POST':
        email = request.form.get('fCorreo')
        emailMinusculas = email.lower()
        user = Usuario.query.filter_by(correoUsuario=email).first()
        if user:
            # Genera un token único
            token = generate_token(email)
            
            # Almacena el token en la base de datos
            reset_token = PasswordResetToken(idUsuarioForaneo=user.idUsuario, token=token)
            db.session.add(reset_token)
            db.session.commit()
            
            # Envía un correo electrónico al usuario con el enlace para restablecer la contraseña
            reset_link = url_for('reset_password', token=token, _external=True)#cambiar a https://proyectoformativo.onrender.com/ cuando deploy
            msg = Message('Restablecer contraseña', sender='pruebaemailsconfirmacion@gmail.com', recipients=[emailMinusculas])
            msg.body = f'Para restablecer tu contraseña, visita el siguiente enlace: {reset_link}'
            mail.send(msg)
            flash('Se ha enviado un correo electrónico con instrucciones para restablecer la contraseña.', 'success')
            return redirect(url_for('usuario.login'))
        else:
            flash('El correo electrónico proporcionado no está registrado.', 'warning')
            return redirect(request.url)
    return render_template('auth/reset_password.html')

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    logout_user()
    if request.method == 'POST':
        password = request.form.get('fContraseña')
        confirm_password = request.form.get('fConfirmarContraseña')
        if not password and not confirm_password:
            flash('La nueva contraseña no puede estar vacia', 'warning')
            redirect(request.url)
        elif password == confirm_password:
            # Busca el token en la base de datos
            reset_token = PasswordResetToken.query.filter_by(token=token).first()
            if reset_token:
                if reset_token.timestamp < datetime.now() - timedelta(minutes=30):
                    # Elimina el token de la base de datos
                    db.session.delete(reset_token)
                    db.session.commit()
                    flash("El token de restablecimiento de contraseña ha expirado.", "error")
                    return redirect(url_for('usuario.login'))
                # Realiza el restablecimiento de la contraseña
                user = Usuario.query.get(reset_token.idUsuarioForaneo)
                contraseña_encriptada = generate_password_hash(password)
                user.contraseñaUsuario = contraseña_encriptada
                db.session.commit()
                db.session.delete(reset_token)
                db.session.commit()
                flash("La contraseña ha sido actualizada correctamente", "success")
                return redirect(url_for('usuario.login'))
            else:
                flash ("Este token es inválido o ya fue utilizado.", "error")
                return redirect(request.url)
        else:
            flash ("Las contraseñas no coinciden", "error")
            return redirect(request.url)
    return render_template('auth/reset_password_with_token.html')

with app.app_context():
    Base = declarative_base()
    target_metadata = db.metadata
    db.create_all()
    
    


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))