# 🐍 PythonWeb

Aplicación web desarrollada con **Python y Flask** como proyecto académico para la gestión y desarrollo de funcionalidades web utilizando una arquitectura modular, conexión a base de datos y operaciones CRUD.

El proyecto hace parte del aprendizaje y aplicación práctica de conceptos relacionados con **desarrollo web, sistemas transaccionales, bases de datos y programación backend**.

---

## 📋 Tabla de contenidos

* [Descripción](#-descripción)
* [Características](#-características)
* [Tecnologías utilizadas](#-tecnologías-utilizadas)
* [Requisitos](#-requisitos)
* [Instalación](#-instalación)
* [Configuración](#-configuración)
* [Ejecución](#-ejecución)
* [Estructura del proyecto](#-estructura-del-proyecto)
* [Base de datos](#-base-de-datos)
* [Dependencias](#-dependencias)
* [Solución de problemas](#-solución-de-problemas)
* [Autor](#-autor)

---

## 📖 Descripción

**PythonWeb** es una aplicación web desarrollada utilizando el framework **Flask**, diseñada para poner en práctica el desarrollo de aplicaciones web con Python.

El proyecto utiliza una arquitectura organizada por módulos, permitiendo separar responsabilidades como:

* Configuración de la aplicación.
* Modelos de datos.
* Rutas y lógica de negocio.
* Plantillas HTML.
* Archivos estáticos.
* Conexión y gestión de la base de datos.
* Migraciones de base de datos.

El objetivo principal es contar con una base de aplicación Flask que pueda ser extendida con nuevas funcionalidades y utilizada como proyecto académico y de aprendizaje.

---

## ✨ Características

* 🌐 Aplicación web desarrollada con Flask.
* 🐍 Backend desarrollado en Python.
* 🗄️ Integración con base de datos mediante Flask-SQLAlchemy.
* 🔄 Gestión de modelos y operaciones sobre la base de datos.
* 🧩 Arquitectura modular.
* 🎨 Interfaz web mediante HTML y archivos estáticos.
* 🔐 Manejo de variables de configuración mediante `.env`.
* 📦 Dependencias administradas mediante `requirements.txt`.
* 🔄 Soporte para migraciones de base de datos mediante Alembic/Flask-Migrate.
* 💻 Compatible con Windows, Linux y macOS, siempre que Python y las dependencias requeridas estén instaladas.

---

## 🛠️ Tecnologías utilizadas

| Tecnología                 | Uso                              |
| -------------------------- | -------------------------------- |
| 🐍 Python                  | Lenguaje principal               |
| 🌐 Flask                   | Framework web                    |
| 🗄️ Flask-SQLAlchemy       | ORM y conexión con base de datos |
| 🔄 Flask-Migrate / Alembic | Migraciones de base de datos     |
| 🐘 SQLAlchemy              | ORM                              |
| 🖥️ HTML                   | Estructura de las páginas        |
| 🎨 CSS                     | Estilos de la interfaz           |
| ⚡ JavaScript               | Funcionalidades del frontend     |
| 📦 pip                     | Gestión de dependencias          |
| 🔧 Git / GitHub            | Control de versiones             |

---

# 📋 Requisitos

Antes de instalar el proyecto debes tener instalado:

* **Python 3.12 o superior**
* **Git**
* Una base de datos compatible con la configuración del proyecto.
* `pip`

Puedes comprobar la instalación de Python con:

```bash
python --version
```

Y Git con:

```bash
git --version
```

> **Nota:** Se recomienda utilizar una versión estable de Python compatible con las dependencias definidas en `requirements.txt`.

---

# 🚀 Instalación

## 1. Clonar el repositorio

Clona el proyecto desde GitHub:

```bash
git clone https://github.com/JorgeBestDev/PythonWeb.git
```

Ingresa a la carpeta:

```bash
cd PythonWeb
```

---

## 2. Crear el entorno virtual

### Windows

```powershell
python -m venv venv
```

Activar el entorno:

```powershell
.\venv\Scripts\Activate.ps1
```

Si estás utilizando CMD:

```cmd
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Cu
