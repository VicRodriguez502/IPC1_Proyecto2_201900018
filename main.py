#IMPORTACIONES 
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
from Usuario import Usuario
from Libro import Libro
from Prestamo import Prestamo

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

#MÉTODO POST PARA CREAR USUARIO
@app.route("/crear_usuario", methods = ["POST"])
def CrearUsuario():
    global Usuarios
    id = request.json["id_user"]
    name = request.json["user_display_name"]
    nickname = request.json["user_nickname"]
    password = request.json["user_password"]
    edad = request.json["user_age"]
    carrera = request.json["user_career"]
    carnet = request.json["user_carnet"]
    Usuarios.append(Usuario(id, name, nickname, password, edad, carrera, carnet))
    return(jsonify({
        "status": "200",
        "msg" : "response"
    }))

#********************************************************************************************************
#FORMATO PARA INICIAR NUESTRA API
if __name__ == "__main__":
    app.run(host = "localhost", port = 3000, debug = True)