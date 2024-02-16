from app import create_app,db
import os
from datetime import datetime
from hashlib import sha256
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user
from flask_mail import Mail, Message
from app.models.usuario import Usuario
from app.models.password_reset_token import PasswordResetToken

app = create_app()


def generate_token(email):
    # Genera un token único basado en el correo electrónico del usuario y la fecha actual
    token_data = f"{email}{datetime.now()}"
    return sha256(token_data.encode()).hexdigest()

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password_request():
    if request.method == 'POST':
        email = request.form.get('fCorreo')
        user = Usuario.query.filter_by(correoUsuario=email).first()
        if user:
            # Genera un token único
            token = generate_token(email)
            
            # Almacena el token en la base de datos
            reset_token = PasswordResetToken(idUsuario=user.idUsuario, token=token)
            db.session.add(reset_token)
            db.session.commit()
            
            # Envía un correo electrónico al usuario con el enlace para restablecer la contraseña
            reset_link = url_for('reset_password', token=token, _external=True)
            msg = Message('Restablecer contraseña', sender='jorgito475@gmail.com', recipients=[email])
            msg.body = f'Para restablecer tu contraseña, visita el siguiente enlace: https://proyectoformativo.onrender.com/{reset_link}'
            Mail.send(msg)
            return 'Se ha enviado un correo electrónico con instrucciones para restablecer la contraseña.'
        else:
            return 'El correo electrónico proporcionado no está registrado.'
    usuario=current_user
    print("info de current_user", usuario)
    return render_template('auth/reset_password.html',usuario=usuario)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if request.method == 'POST':
        password = request.form.get('fContraseña')
        confirm_password = request.form.get('fConfirmarContraseña')
        if password == confirm_password:
            # Busca el token en la base de datos
            reset_token = PasswordResetToken.query.filter_by(token=token).first()
            if reset_token:
                # Realiza el restablecimiento de la contraseña
                user = Usuario.query.get(reset_token.idUsuarioForaneo)
                user.password = password
                db.session.delete(reset_token)
                db.session.commit()
                flash("La contraseña ha sido actualizada correctamente", "success")
                return redirect(url_for('usuario.login'))
            else:
                flash ("Este token es inválido o ya fue utilizado.", "danger")
                return redirect(request.url)
        else:
            return 'Las contraseñas no coinciden.'
    return render_template('reset_password_with_token.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))