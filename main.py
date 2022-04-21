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

#***********************************************************
#METODOS Y FUNCIONES PARA USUARIOS

#MÉTODO GET PARA MOSTRAR USUARIOS EN EL SISTEMA (IDEA INNOVADORA)
@app.route("/Usuarios", methods=["GET"])
def MostrarUsuarios():
    global Usuarios
    Dato = []
    for Usuario in Usuarios:
        objeto = {
            "id_user" : Usuario.getId_user(),
            "user_display_name" : Usuario.getUser_display_name(),
            "user_nickname": Usuario.getUser_nickname(),
            "user_password" : Usuario.getUser_password(),
            "user_age" : Usuario.getUser_age(),
            "user_career": Usuario.getUser_career(),
            "user_carnet" : Usuario.getUser_carnet()
        }
        Dato.append(objeto)
    return(jsonify(Dato))

#MÉTODO POST PARA CREAR USUARIO
@app.route("/crear_usuario", methods = ["POST"])
def CrearUsuario():
    global Usuarios
    try:
        id = request.json["id_user"]
        name = request.json["user_display_name"]
        nickname = request.json["user_nickname"]
        password = request.json["user_password"]
        edad = request.json["user_age"]
        carrera = request.json["user_career"]
        carnet = request.json["user_carnet"]
        if ValidarIDusuario(id) == True:
            return(jsonify({
            "msg": "El ID de Usuario ya existe, intente con otro"
            })) 
        else:
            Usuarios.append(Usuario(id, name, nickname, password, edad, carrera, carnet))
            return(jsonify({
            "status": "200",
            "msg" : "response"
        }))
    except:
        pass


#FUNCIÓN PARA VALIDAD UN SOLO ID
def ValidarIDusuario(id):
    global Usuarios
    for i in range(len(Usuarios)):
        if id == Usuarios[i].getId_user():
            return True
        else: 
            return False

#METODO POST PARA VALIDAR EL USUARIO 
@app.route("/validacion_usuario", methods = ["POST"])
def VerificarUser():
    global Usuarios
    nickname = request.json["user_nickname"]
    for i in range(len(Usuarios)):
        if nickname == Usuarios[i].getUser_nickname():
            Dato = []
            for Usuario in Usuarios:
                objeto = {
                    "id_user" : Usuario.getId_user(),
                    "user_display_name" : Usuario.getUser_display_name(),
                    "user_nickname": Usuario.getUser_nickname(),
                    "user_password" : Usuario.getUser_password(),
                    "user_age" : Usuario.getUser_age(),
                    "user_career": Usuario.getUser_career(),
                    "user_carnet" : Usuario.getUser_carnet()
                }
            Dato.append(objeto)
            return(jsonify(Dato))
        return(jsonify({
            "Mensaje" : "El Usuario no existe dentro de nuestra base de datos"
            }))
    
#**********************************************
#METODOS Y FUNCIONES PARA LIBROS

#METODO PARA CREAR UN LIBRO NUEVO
@app.route("/crear_libro", methods = ["POST"])
def CrearLibro():
    global Libros
    id = request.json["id_book"]
    titulo = request.json["book_title"]
    type = request.json["book_type"]
    autor = request.json["author"]
    count = request.json["book_count"]
    available = request.json["book_available"]
    noavailable = request.json["book_not_available"]
    year = request.json["book_year"]
    editorial = request.json["book_editorial"]
    Usuarios.append(Usuario(id, titulo, type, autor, count, available, noavailable, year, editorial))
    return(jsonify({
        "status": "200",
        "msg" : "response"
    }))

#METODO PARA VERIFICAR SI EL ID DEL LIBRO EXISTE
def VerificarIDlibro(idlib):
    global Libros
    validar = False
    for ilib in Usuarios:
        if str(idlib) == str(ilib.getID_book()):
            validar =True
    return validar

#********************************************************************************************************
#FORMATO PARA INICIAR NUESTRA API
if __name__ == "__main__":
    app.run(host = "localhost", port = 3000, debug = True)