import os
import secrets
from datetime import timedelta
#kqra jnuo zayw sixi
SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(32))
PERMANENT_SESSION_LIFETIME = timedelta(days=365)
UPLOAD_FOLDER= 'app/static/images/productos'


#credenciales base de datos db4free.net
#nombre base de datos: proyecto_python
#Nombre de usuario MySQL: admin34587209
#Contraseña de usuario MySQL:@Bh!5H2$9Lqz&7pX
#correo administrador web: administrador@tiendaonline.com
#contraseña administrador web: W#u8@r!P5b2$qF9Z
#consulta para insertar paises y administrador: INSERT INTO pais VALUES (null, 'Afganistán'), (null, 'Albania'), (null, 'Alemania'), (null, 'Andorra'), (null, 'Angola'), (null, 'Antigua y Barbuda'), (null, 'Arabia Saudita'), (null, 'Argelia'), (null, 'Argentina'), (null, 'Armenia'), (null, 'Australia'), (null, 'Austria'), (null, 'Azerbaiyán'), (null, 'Bahamas'), (null, 'Bangladés'), (null, 'Barbados'), (null, 'Baréin'), (null, 'Bélgica'), (null, 'Belice'), (null, 'Benín'), (null, 'Bielorrusia'), (null, 'Birmania (Myanmar)'), (null, 'Bolivia'), (null, 'Bosnia y Herzegovina'), (null, 'Botsuana'), (null, 'Brasil'), (null, 'Brunéi'), (null, 'Bulgaria'), (null, 'Burkina Faso'), (null, 'Burundi'), (null, 'Bután'), (null, 'Cabo Verde'), (null, 'Camboya'), (null, 'Camerún'), (null, 'Canadá'), (null, 'Catar'), (null, 'Chad'), (null, 'Chile'), (null, 'China'), (null, 'Chipre'), (null, 'Ciudad del Vaticano (Santa Sede)'), (null, 'Colombia'), (null, 'Comoras'), (null, 'Corea del Norte'), (null, 'Corea del Sur'), (null, 'Costa de Marfil'), (null, 'Costa Rica'), (null, 'Croacia'), (null, 'Cuba'), (null, 'Dinamarca'), (null, 'Dominica'), (null, 'Ecuador'), (null, 'Egipto'), (null, 'El Salvador'), (null, 'Emiratos Árabes Unidos'), (null, 'Eritrea'), (null, 'Eslovaquia'), (null, 'Eslovenia'), (null, 'España'), (null, 'Estados Unidos'), (null, 'Estonia'), (null, 'Etiopía'), (null, 'Filipinas'), (null, 'Finlandia'), (null, 'Fiyi'), (null, 'Francia'), (null, 'Gabón'), (null, 'Gambia'), (null, 'Georgia'), (null, 'Ghana'), (null, 'Granada'), (null, 'Grecia'), (null, 'Guatemala'), (null, 'Guinea'), (null, 'Guinea Ecuatorial'), (null, 'Guinea-Bisáu'), (null, 'Guyana'), (null, 'Haití'), (null, 'Honduras'), (null, 'Hungría'), (null, 'India'), (null, 'Indonesia'), (null, 'Irak'), (null, 'Irán'), (null, 'Irlanda'), (null, 'Islandia'), (null, 'Islas Marshall'), (null, 'Islas Salomón'), (null, 'Israel'), (null, 'Italia'), (null, 'Jamaica'), (null, 'Japón'), (null, 'Jordania'), (null, 'Kazajistán'), (null, 'Kenia'), (null, 'Kirguistán'), (null, 'Kiribati'), (null, 'Kuwait'), (null, 'Laos'), (null, 'Lesoto'), (null, 'Letonia'), (null, 'Líbano'), (null, 'Liberia'), (null, 'Libia'), (null, 'Liechtenstein'), (null, 'Lituania'), (null, 'Luxemburgo'), (null, 'Macedonia del Norte'), (null, 'Madagascar'), (null, 'Malasia'), (null, 'Malaui'), (null, 'Maldivas'), (null, 'Malí'), (null, 'Malta'), (null, 'Marruecos'), (null, 'Mauricio'), (null, 'Mauritania'), (null, 'México'), (null, 'Micronesia'), (null, 'Moldavia'), (null, 'Mónaco'), (null, 'Mongolia'), (null, 'Montenegro'), (null, 'Mozambique'), (null, 'Namibia'), (null, 'Nauru'), (null, 'Nepal'), (null, 'Nicaragua'), (null, 'Níger'), (null, 'Nigeria'), (null, 'Noruega'), (null, 'Nueva Zelanda'), (null, 'Omán'), (null, 'Países Bajos'), (null, 'Pakistán'), (null, 'Palaos'), (null, 'Panamá'), (null, 'Papúa Nueva Guinea'), (null, 'Paraguay'), (null, 'Perú'), (null, 'Polonia'), (null, 'Portugal'), (null, 'Reino Unido'), (null, 'República Centroafricana'), (null, 'República Checa'), (null, 'República del Congo'), (null, 'República Democrática del Congo'), (null, 'República Dominicana'), (null, 'República Sudafricana'), (null, 'Ruanda'), (null, 'Rumania'), (null, 'Rusia'), (null, 'Samoa'), (null, 'San Cristóbal y Nieves'), (null, 'San Marino'), (null, 'San Vicente y las Granadinas'), (null, 'Santa Lucía'), (null, 'Santo Tomé y Príncipe'), (null, 'Senegal'), (null, 'Serbia'), (null, 'Seychelles'), (null, 'Sierra Leona'), (null, 'Singapur'), (null, 'Siria'), (null, 'Somalia'), (null, 'Sri Lanka'), (null, 'Suazilandia (Eswatini)'), (null, 'Sudán'), (null, 'Sudán del Sur'), (null, 'Suecia'), (null, 'Suiza'), (null, 'Surinam'), (null, 'Tailandia'), (null, 'Tanzania'), (null, 'Tayikistán'), (null, 'Timor Oriental'), (null, 'Togo'), (null, 'Tonga'), (null, 'Trinidad y Tobago'), (null, 'Túnez'), (null, 'Turkmenistán'), (null, 'Turquía'), (null, 'Tuvalu'), (null, 'Ucrania'); insert into usuario values (1, 'Administrador', 'administrador@tiendaonline.com', 'scrypt:32768:8:1$l3kNvbbSLHpnZDZe$192ee8d615806f7217a2101b7c752579e2a4fc0d2032075e8b0baa1fca07b60a63b175bf80c74b9ae0738fdbb0524f2e8fc3aec6224d92d760dc17c2c804ff94', null, null, 42, '', '', '',1, true)
#contraseña hasheada scrypt:32768:8:1$l3kNvbbSLHpnZDZe$192ee8d615806f7217a2101b7c752579e2a4fc0d2032075e8b0baa1fca07b60a63b175bf80c74b9ae0738fdbb0524f2e8fc3aec6224d92d760dc17c2c804ff94

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:efHgaH1ccade5H1Ea32-HAhHehfHD4Eb@roundhouse.proxy.rlwy.net:56177/proyecto_formativo'
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'pruebaemailsconfirmacion@gmail.com')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'kqrajnuozaywsixi')

