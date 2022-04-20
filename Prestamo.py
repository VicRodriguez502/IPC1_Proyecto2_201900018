#CREANDO CLASE PRESTAMO
class Prestamo():
    
    #CONSTRUCTOR PARA LA CLASE PRESTAMO
    def __init__ (self,id_loan,loan_date):
        self.id_loan = id_loan
        self.loan_date = loan_date
    
    #ENCAPSULAMIENTO PARA LOS PARAMETROS DE PRESTAMO
    def getID_loan(self):
        return self.id_loan
    
    def getLoan_date(self):
        return self.loan_date
    
    def setID_loan(self, id_loan):
        self.id_loan = id_loan
    
    def setLoan_date(self, loan_date):
        self.loan_date = loan_date