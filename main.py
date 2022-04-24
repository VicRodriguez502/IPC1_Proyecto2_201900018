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

Libros.append(Libro(1,"Don Quijote", "Libro", "Miguel de Cervantes", "50", "25", "25", "1990", "Española"))
Libros.append(Libro(2, "Viajes Extraordinarios", "Libro Electronico", "Luisito comunica", "100", "80", "20", "2019", "Mexico"))

Usuarios.append(Usuario(1, "Victor Rodriguez", "TheKing502", "123456", "25", "Ingenieria en ciencias y Sistemas", "201900018"))

#*******************************************************************************************************
#CREACIÓN API 
app = Flask(__name__)
CORS(app)

#*******************************************************************************************************
#CUERPO DE METODOS PARA LA API
@app.route("/", methods = ["GET"])
def iniciar():
    return "BIENVENIDO AL PROYECTO 2 DE IPC1"

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
    return(jsonify(Dato)),200

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
        if ValidarIDusuario(id) == False:
            Usuarios.append(Usuario(id, name, nickname, password, edad, carrera, carnet))
            return(jsonify({
            "status": "200",
            "msg": "El usuario se ha creado correctamente"
            })),200 
        else:
            return(jsonify({
                "status": "400",
                "msg" : "El ID de Usuario ya existe, intente con otro"
            })),400
    except:
        pass


#FUNCIÓN PARA VALIDAD QUE NO SE REPITA EL ID USUARIO
def ValidarIDusuario(n):
    global Usuarios
    valido = False
    for Usuario in Usuarios:
        if str(n) == str(Usuario.getId_user()):
            valido =True
    return valido

#METODO POST PARA VALIDAR EL USUARIO 
@app.route("/validacion_usuario", methods = ["POST"])
def VerificarUser():
    global Usuarios
    nickname = request.json["user_nickname"]
    password = request.json["user_password"]
    for i in range(len(Usuarios)):
        if nickname == Usuarios[i].getUser_nickname():
            if password == Usuarios[i].getUser_password():
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
                return(jsonify(Dato)),200
            else: return(jsonify({
                "status": "400",
                "Mensaje" : "La contraseña no existe dentro de nuestra base de datos"
                })),400
        return(jsonify({
            "status": "400",
            "Mensaje" : "El Usuario no existe dentro de nuestra base de datos"
            })),400
    
#**********************************************
#METODOS Y FUNCIONES PARA LIBROS

#MÉTODO GET PARA MOSTRAR Libros EN EL SISTEMA (IDEA INNOVADORA)
@app.route("/Libros", methods=["GET"])
def MostrarLibros():
    global Libros
    Dato = []
    for lib in Libros:
        objeto = {
            "id_book" : lib.getID_book(),
            "book_title" : lib.getBOOK_title(),
            "book_type": lib.getBOOK_type(),
            "author" : lib.getAuthor(),
            "book_count" : lib.getBOOK_count(),
            "book_available" : lib.getBOOK_available(),
            "book_not_available" : lib.getBOOK_not_available(),
            "book_year" : lib.getBOOK_year(),
            "user_editorial": lib.getBOOK_editorial(),
        }
        Dato.append(objeto)
    return(jsonify(Dato)),200

#METODO PARA CREAR UN LIBRO NUEVO
@app.route("/crearlibro", methods = ["POST"])
def CrearLibro2():
    global Libros
    try:
        id1 = request.json["id_book"]
        titulo = request.json["book_title"]
        type = request.json["book_type"]
        autor = request.json["author"]
        count = request.json["book_count"]
        available = request.json["book_available"]
        noavailable = request.json["book_not_available"]
        year = request.json["book_year"]
        editorial = request.json["book_editorial"]
        if Reviso(id1) == False:
            Libros.append(Libro(id1, titulo, type, autor, count, available, noavailable, year, editorial))
            return(jsonify({
                "status": "200",
                "msg" : "Se creo el Libro Correctamente"
            })),200
        else:
            
            return(jsonify({
                "status": "200",
                "msg" : "El ID de Libro ya existe, intente con otro"
            })),400
    except:
        pass

#FUNCIÓN PARA VALIDAD QUE NO SE REPITA ID LIBRO
def Reviso(n):
    global Libros
    valido = False
    for Libro in Libros:
        if str(n) == str(Libro.getID_book()):
            valido =True
    return valido
        

#MÉTODO PARA ACTUALIZAR UN LIBRO
@app.route("/actualizarlibro/<int:id>", methods = ["PUT"])
def ActualizarLibro(id):
    global Libros
    idlib = request.json["id_book"]
    title = request.json["book_title"]
    type = request.json["book_type"]
    author = request.json["author"]
    count = request.json["book_count"]
    available = request.json["book_available"]
    navailable = request.json["book_not_available"]
    anio = request.json["book_year"]
    editorial = request.json["book_editorial"]
    for i in range(len(Libros)):
        if id == int(Libros[i].getID_book()):
            Libros[i].setID_book(idlib)
            Libros[i].setBook_title(title)
            Libros[i].setBook_type(type)
            Libros[i].setAuthor(author)
            Libros[i].setBook_count(count)
            Libros[i].setBook_available(available)
            Libros[i].setBook_not_available(navailable)
            Libros[i].setBook_year(anio)
            Libros[i].setBook_editorial(editorial)
            return(jsonify({
                "status": 200,
                "msg": "Se actualizo el Libro Correctamente"
            })),200
    return(jsonify({
        "status": 400,
        "msg": "No se pudo actualizar el Libro"
    }))

#METODO GET PARA VER LIBROS SEGUN SI ID, TIPO O TITULO
@app.route("/verlibro", methods=["GET"])
def VerLibro():
    global Libros
    idlib = None
    tipo = None
    titulo = None
    try:
        try:
            idlib = request.json["id_book"]
        except:
            idlib = None
        try:
            tipo = request.json["book_type"]
        except:
            tipo = None
        try:
            titulo = request.json["book_title"]
        except:
            titulo = None
        if idlib !=None:
            for i in range(len(Libros)):
                if idlib == Libros[i].getID_book():
                    datos={
                        "id_book":Libros[i].getID_book(),
                        "book_title":Libros[i].getBOOK_title(),
                        "book_type": Libros[i].getBOOK_type(),
                        "author": Libros[i].getAuthor(),
                        "book_count": Libros[i].getBOOK_count(),
                        "book_available": Libros[i].getBOOK_available(),
                        "book_not_available": Libros[i].getBOOK_not_available(),
                        "book_year":Libros[i].getBOOK_year(),
                        "book_editorial": Libros[i].getBOOK_editorial()
                    }
                    return(jsonify(datos))
                
            return(jsonify({
                "Mensaje":"No se encontró el id"
                    })),400
        elif idlib == None and tipo !=None and titulo == None:
            type = []
            for i in range(len(Libros)):
                if tipo == Libros[i].getBOOK_type():
                    datos1={
                        "id_book":Libros[i].getID_book(),
                        "book_title":Libros[i].getBOOK_title(),
                        "book_type": Libros[i].getBOOK_type(),
                        "author": Libros[i].getAuthor(),
                        "book_count": Libros[i].getBOOK_count(),
                        "book_available": Libros[i].getBOOK_available(),
                        "book_not_available": Libros[i].getBOOK_not_available(),
                        "book_year":Libros[i].getBOOK_year(),
                        "book_editorial": Libros[i].getBOOK_editorial()
                    }
                    type.append(datos1)
            if len(type) == 0:
                return(jsonify({
                    "Mensaje":"No se encontró el tipo"
                        })),400
            else:
                return(jsonify(type)),200
        elif idlib == None and tipo == None and titulo != None:
            title = []
            for i in range(len(Libros)):
                if titulo == Libros[i].getBOOK_title():
                    datos2 = {
                        "id_book":Libros[i].getID_book(),
                        "book_title":Libros[i].getBOOK_title(),
                        "book_type": Libros[i].getBOOK_type(),
                        "author": Libros[i].getAuthor(),
                        "book_count": Libros[i].getBOOK_count(),
                        "book_available": Libros[i].getBOOK_available(),
                        "book_not_available": Libros[i].getBOOK_not_available(),
                        "book_year":Libros[i].getBOOK_year(),
                        "book_editorial": Libros[i].getBOOK_editorial()
                    }
                    title.append(datos2)
            if len(title) == 0:
                return(jsonify({
                    "Mensaje":"No se encontró el titulo"
                        })),400
            else:
                return(jsonify(title)),200
    except:
        return(jsonify({
            "Mensaje":"Por favor ingresa json valido"
                })),400



#********************************************************************************************************
#FORMATO PARA INICIAR NUESTRA API
if __name__ == "__main__":
    app.run(host = "localhost", port = 3000, debug = True)