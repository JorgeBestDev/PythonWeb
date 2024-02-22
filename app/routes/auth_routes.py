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
from app.models.pais import Pais
from app.models.producto import Producto
from app.models.carrito import Carrito
from app.models.pedido import Pedido
from sqlalchemy.exc import IntegrityError



bp = Blueprint("auth", __name__)



@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form["first-name"]
        last_name = request.form["last-name"]
        correoUsuario = request.form["fCorreoUsuario"]
        contraseñaUsuario = request.form["fContraseña"]
        telefonoUsuario = request.form["fTelefonoUsuario"]
        pais = request.form["fPais"]
        direccion = request.form["fDireccion"]
        ciudad = request.form["fCiudad"]
        estado = request.form["fEstado"]
        codigoPostal = request.form["fCodigoPostal"]

        if not all(
            [
                first_name,
                last_name,
                correoUsuario,
                contraseñaUsuario,
                telefonoUsuario,
                pais,
                direccion,
                ciudad,
                estado,
                codigoPostal,
            ]
        ):
            flash("Por favor, completa todos los campos del formulario.", "error")
            return redirect(request.url)

        nombreUsuario = f"{first_name} {last_name}"  # Concatenar nombre de usuario

        contraseña_encriptada = generate_password_hash(contraseñaUsuario)

        user = Usuario(
            nombreUsuario=nombreUsuario,
            correoUsuario=correoUsuario,
            contraseñaUsuario=contraseña_encriptada,
            telefonoUsuario=telefonoUsuario,
            pais_id=pais,
            direccion=direccion,
            estado=estado,
            ciudad=ciudad,
            codigoPostal=codigoPostal,
        )

        try:
            db.session.add(user)
            db.session.commit()
            flash("Usuario registrado", "success")
            return render_template("auth/login.html")
        except IntegrityError:
            db.session.rollback()
            flash("Correo ya existente", "error")
            return redirect(request.url)
    paises = Pais.query.all()
    return render_template("auth/register.html", paises=paises)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        correo = request.form["fCorreoUsuario"]
        contraseña = request.form["fContraseñaUsuario"]
        user = Usuario.query.filter_by(correoUsuario=correo).first()
        
        if not user:  
            flash('No hay ningún correo asociado a tu cuenta.', 'error')
            return redirect(request.url)
        
        if user.es_administrador==1 and check_password_hash(user.contraseñaUsuario, contraseña):
            login_user(user)
            print("current user admin: ", current_user)
            return redirect(url_for('auth.index'))
        
        if  user.es_administrador==0 and check_password_hash(user.contraseñaUsuario, contraseña):
            login_user(user)
            print("current user usuario: ", current_user)
            return redirect(url_for("auth.index"))   
        
    return render_template("auth/login.html")


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.index"))


@bp.route("/")
def index():
    contraseña ='W#u8@r!P5b2$qF9Z'
    contraseña_hash=generate_password_hash(contraseña)
    print(contraseña_hash)
    productos = Producto.query.all()
    carrito = Carrito.query.all()
    pedido=Pedido.query.all()
    usuarioActual = current_user
    if usuarioActual.is_authenticated:
        cantidad_pedidos = Pedido.query.filter_by(usuarioForeaneo=usuarioActual.idUsuario).count()
    else:
        cantidad_pedidos = 0
    
    print("pedidos: ",carrito)
    return render_template("index.html", current_user=usuarioActual, productos=productos, carrito=carrito, cantidad_pedidos=cantidad_pedidos)