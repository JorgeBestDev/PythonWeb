from flask_login import (
    login_required,
    login_manager,
    UserMixin,
    login_user,
    logout_user,
    current_user,
)
from sqlalchemy import text
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
    if request.method == "GET":
        paises = [
            'Afganistán', 'Albania', 'Alemania', 'Andorra', 'Angola', 'Antigua y Barbuda', 'Arabia Saudita',
            'Argelia', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaiyán', 'Bahamas', 'Bangladés',
            'Barbados', 'Baréin', 'Bélgica', 'Belice', 'Benín', 'Bielorrusia', 'Birmania (Myanmar)', 'Bolivia',
            'Bosnia y Herzegovina', 'Botsuana', 'Brasil', 'Brunéi', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Bután',
            'Cabo Verde', 'Camboya', 'Camerún', 'Canadá', 'Catar', 'Chad', 'Chile', 'China', 'Chipre',
            'Ciudad del Vaticano (Santa Sede)', 'Colombia', 'Comoras', 'Corea del Norte', 'Corea del Sur',
            'Costa de Marfil', 'Costa Rica', 'Croacia', 'Cuba', 'Dinamarca', 'Dominica', 'Ecuador', 'Egipto',
            'El Salvador', 'Emiratos Árabes Unidos', 'Eritrea', 'Eslovaquia', 'Eslovenia', 'España', 'Estados Unidos',
            'Estonia', 'Etiopía', 'Filipinas', 'Finlandia', 'Fiyi', 'Francia', 'Gabón', 'Gambia', 'Georgia', 'Ghana',
            'Granada', 'Grecia', 'Guatemala', 'Guinea', 'Guinea Ecuatorial', 'Guinea-Bisáu', 'Guyana', 'Haití',
            'Honduras', 'Hungría', 'India', 'Indonesia', 'Irak', 'Irán', 'Irlanda', 'Islandia', 'Islas Marshall',
            'Islas Salomón', 'Israel', 'Italia', 'Jamaica', 'Japón', 'Jordania', 'Kazajistán', 'Kenia',
            'Kirguistán', 'Kiribati', 'Kuwait', 'Laos', 'Lesoto', 'Letonia', 'Líbano', 'Liberia', 'Libia',
            'Liechtenstein', 'Lituania', 'Luxemburgo', 'Macedonia del Norte', 'Madagascar', 'Malasia', 'Malaui',
            'Maldivas', 'Malí', 'Malta', 'Marruecos', 'Mauricio', 'Mauritania', 'México', 'Micronesia', 'Moldavia',
            'Mónaco', 'Mongolia', 'Montenegro', 'Mozambique', 'Namibia', 'Nauru', 'Nepal', 'Nicaragua', 'Níger',
            'Nigeria', 'Noruega', 'Nueva Zelanda', 'Omán', 'Países Bajos', 'Pakistán', 'Palaos', 'Panamá',
            'Papúa Nueva Guinea', 'Paraguay', 'Perú', 'Polonia', 'Portugal', 'Reino Unido', 'República Centroafricana',
            'República Checa', 'República del Congo', 'República Democrática del Congo', 'República Dominicana',
            'República Sudafricana', 'Ruanda', 'Rumania', 'Rusia', 'Samoa', 'San Cristóbal y Nieves', 'San Marino',
            'San Vicente y las Granadinas', 'Santa Lucía', 'Santo Tomé y Príncipe', 'Senegal', 'Serbia', 'Seychelles',
            'Sierra Leona', 'Singapur', 'Siria', 'Somalia', 'Sri Lanka', 'Suazilandia (Eswatini)', 'Sudán',
            'Sudán del Sur', 'Suecia', 'Suiza', 'Surinam', 'Tailandia', 'Tanzania', 'Tayikistán', 'Timor Oriental',
            'Togo', 'Tonga', 'Trinidad y Tobago', 'Túnez', 'Turkmenistán', 'Turquía', 'Tuvalu', 'Ucrania'
        ]

        for i, pais in enumerate(paises, start=1):
            # Comprobar si el idPais ya existe
            query_check = text("SELECT idPais FROM pais WHERE idPais = :id")
            result = db.session.execute(query_check, {'id': i}).fetchone()

            # Si no existe, realizar la inserción
            if not result:
                try:
                    query_insert = text("INSERT INTO pais (idPais, nombrePais) VALUES (:id, :nombre)")
                    db.session.execute(query_insert, {'id': i, 'nombre': pais})
                    db.session.commit()
                except IntegrityError as e:
                    print(f"Error insertando país {pais}: {e}")
                
        
        administrador = Usuario(
            idUsuario="1",
            nombreUsuario="Administrador",
            correoUsuario="administrador@tiendaonline.com",
            contraseñaUsuario="W#u8@r!P5b2$qF9Z",
            pais_id=1,
            direccion="Nulo",
            estado="Nulo",
            ciudad="Nulo",
            codigoPostal="0",
            es_administrador=True
        )
        try:
            admin = Usuario.query.filter(Usuario.idUsuario==1)
            if not(admin):
                db.session.add(administrador)
                db.session.commit()
        except IntegrityError as e:
            print("error al regitrar administrador", e)
        return render_template("auth/login.html")
        
            
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
        


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.index"))


@bp.route("/")
def index():
    #contraseña ='W#u8@r!P5b2$qF9Z'
    #contraseña_hash=generate_password_hash(contraseña)
    #print(contraseña_hash)
    productos = Producto.query.all()
    carrito = Carrito.query.all()
    usuarioActual = current_user
    if usuarioActual.is_authenticated:
        cantidad_pedidos = Pedido.query.filter_by(usuarioForaneo=usuarioActual.idUsuario).count()
    else:
        cantidad_pedidos = 0
    
    print("pedidos: ",carrito)
    return render_template("index.html", current_user=usuarioActual, productos=productos, carrito=carrito, cantidad_pedidos=cantidad_pedidos)