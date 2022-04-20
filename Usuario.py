#CREACIÓN DE LA CLASE USUARIO 
class Usuario():
    
    #CONSTRUCTOR PARA LA CLASE USUARIOS
    def __init__ (self, id_user, user_display_name, user_nickname, user_password, user_age, user_career, user_carnet):
        self.id_user = id_user
        self.user_display_name = user_display_name
        self.user_nickname = user_nickname
        self.user_password = user_password
        self.user_age = user_age
        self.user_career = user_career
        self.user_carnet = user_carnet
    
    #ENCAPSULAMIENTO DE LOS PARAMETROS DEL USUARIO
    #ENCAPSULAMIENTO GET
    def getId_user(self):
        return self.id_user
    
    def getUser_display_name(self):
        return self.user_display_name
    
    def getUser_nickname(self):
        return self.user_nickname
    
    def getUser_password(self):
        return self.user_password
    
    def getUser_age(self):
        return self.user_age
    
    def getUser_career(self):
        return self.user_career
    
    def getUser_carnet(self):
        return self.user_carnet
    
    #ENCAPSULAMIENTO SET
    def setId_user(self, id_user):
        self.id_user = id_user
    
    def setUser_display_name(self, user_display_name):
        self.user_display_name = user_display_name
    
    def setUser_nickname(self, user_nickname):
        self.user_nickname = user_nickname
    
    def setUser_password(self, user_password):
        self.user_password = user_password
    
    def setUser_age(self, user_age):
        self.user_age = user_age
    
    def setUser_career(self, user_career):
        self.user_career = user_career
    
    def setUser_carnet(self, user_carnet):
        self.user_carnet = user_carnet