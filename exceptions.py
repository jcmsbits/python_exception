
# Para darle claridad al código se debe agregar Exception en el nombre
# de la clase
class UsernameCodyException(Exception):
    
    def __init__(self):
        self.message = "El username no puede ser Cody"
        super().__init__(self.message)

class UsernameLenException(Exception):
    
    def __init__(self, username):
        super().__init__(f'El apodo: {username} debe poseer una longitud mayor igual a 6')
        # self.username = username
        #self.message = f'El username: {self.username} debe poseer una longitud mayor igual a 6'
        #print(self.message)
        

class CustomError_1Exception(Exception):

    def __init__(self, *args):
        super().__init__("Error numero 1")

class CustomError_2Exception(Exception):

    def __init__(self, *args):
        super().__init__("Error numero 2")
    
class CustomError_3Exception(Exception):

    def __init__(self, *args):
        super().__init__("Error numero 3")