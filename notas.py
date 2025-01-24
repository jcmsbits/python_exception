
class UsernameException(Exception):

    def __init__(self, *args):
        super().__init__("El username no es valido")

    
    # Las funciones en python que empiezan y terminan con __
    # debemos evitar utilizarlo fuera de la clase

    def is_valid_to_raise(self):
        return len(self.__notes__) > 0

    def show_notes(self):
        for note in self.__notes__:
            print(">>>", note)


def username_validation(username):

    username_error = UsernameException()

    if len(username) <= 5:
        username_error.add_note("La longitud debe ser mayor a 5.")

    if username.lower() == "cody":
        username_error.add_note("El username no puede ser cody")
    
    if "@" == username:
        username_error.add_note("El signo @ no puede encontrarse en el username")

    if username_error.is_valid_to_raise():
        raise username_error

    return True

try:
    username = "cody"    
    username_validation(username) 

except UsernameException as error:
    print(error)
    error.show_notes()