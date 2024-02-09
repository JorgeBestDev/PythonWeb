from flask import Blueprint, render_template, session
from app import db
from app.models.pais import Pais


bp = Blueprint('pais', __name__)