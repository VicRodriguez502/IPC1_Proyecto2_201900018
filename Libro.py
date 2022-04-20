#CREACIÓN DE LA CLASE LIBROS
class Libro():
    
    #CONSTRUCTOR PARA LA CLASE LIBROS
    def __init__(self, id_book, book_title, book_type, author, book_count, book_available, book_not_available, book_year, book_editorial):
        self.id_book = id_book
        self.book_title = book_title
        self.book_type = book_type
        self.author = author
        self.book_count = book_count
        self.book_available = book_available
        self.book_not_available = book_not_available
        self.book_year = book_year
        self.book_editorial = book_editorial
    
    #ENCAPSULAMIENTO PARA LOS PARAMETROS DE LIBROS
    #ENCAPSULAMIENTO GET
    def getID_book(self):
        return self.id_book
    
    def getBOOK_title(self):
        return self.book_title
    
    def getBOOK_type(self):
        return self.book_type
    
    def getAuthor(self):
        return self.author
    
    def getBOOK_count(self):
        return self.book_count
    
    def getBOOK_available(self):
        return self.book_available
    
    def getBOOK_not_available(self):
        return self.book_not_available
    
    def getBOOK_year(self):
        return self.book_year
    
    def getBOOK_editorial(self):
        return self.book_editorial
    
    #ENCAPSULAMIENTO SET
    def setID_book(self, id_book):
        self.id_book = id_book
    
    def setBook_title(self, book_title):
        self.book_title = book_title
    
    def setAuthor(self, author):
        self.author = author
        
    def setBook_count(self, book_count):
        self.book_count = book_count
    
    def setBook_available(self, book_available):
        self.book_available = book_available
    
    def setBook_not_available(self, book_not_available):
        self.book_not_available = book_not_available
    
    def setBook_year(self, book_year):
        self.book_year = book_year
    
    def setBook_editorial(self, book_editorial):
        self.book_editorial = book_editorial