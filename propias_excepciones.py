# POO
from exceptions import UsernameCodyException, UsernameLenException
   
def validate_username(username):

    if username == "cody":
        # raise UsernameCodyException("El username no puede ser Cody.")
        raise UsernameCodyException()

    if len(username) < 6:
        # return False
        # raise UsernameLenException("El username debe tener una longitud mayor a 6 caracteres.")
        raise UsernameLenException(username)
    
    return True

try:
    result = validate_username("cody")
    print(result)

except UsernameCodyException as error:
    # print("El username no puede ser Cody.")
    print(error)

except UsernameLenException as error:
    # print("El username debe tener una longitud mayor a 6 caracteres.")
    print(error)

except Exception as error:
    print(">>> Lo sentimos, no fue posible completar la operación.")
    print(error)