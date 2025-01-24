# POO -> Herencia -> Exception -> BaseException
# BaseException es la clase principal pero se debe usar Exception
try:
    numbers = [0,1,2,3,4,5]

    number1 = numbers[0]
    # number2 = numbers[10]
    number2 = numbers[0]

    result = number1 / number2

# Exception es la clase padre de ZeroDivisionError, NameError, IndexError, etc...
except Exception as error:
    print("No se puede hacer la división por cero")
    print(error)