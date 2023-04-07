from flask import Flask


app = Flask(__name__)



"""Dentro desse arquivo temos que importar o arquivo default.py
da pasta controllers"""

from app.controllers import default

