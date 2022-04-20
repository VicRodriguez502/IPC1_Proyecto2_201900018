#IMPORTACIONES 
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
from Usuario import Usuario
from Libro import Libro
form Prestamo import Prestamo

#*******************************************************************************************************
#CREACIÓN DE LA LISTAS PARA USUARIOS Y LIBROS
Usuarios = []
Libros = []
Prestamos = []

#*******************************************************************************************************
#CREACIÓN API 
app = Flask(__name__)
CORS(app)

#*******************************************************************************************************
#CUERPO DE METODOS PARA LA API
@app.route("/", methods = ["GET"])
def iniciar():
    return "Servidor se ha Iniciado"

#********************************************************************************************************
#FORMATO PARA INICIAR NUESTRA API
if __name__ == "__main__":
    app.run(host = "localhost", port = 3000, debug = True)