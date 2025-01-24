# El traceback nos da un seguimiendo de donde salió el error
# para poder debuguear más rápido

# Para trabjar con la excepciones con Python obligatoriamente
# vamos a tener que trabajar con dos bloques Try - Except

# En Try ponemos el código que puede dar error
# Y en Except lo que queremos que se ejecute si da el error

try:
    numbers = [0,1,2,3,4,5,6,7,8]

    num_1 = 10
    num_2 = 0
    num_3 = 3
    num_5 = numbers[10]


    # result = num_1 / num_2
    # result = num_1 / num_3
    # result = num_1 / num_4
    result = num_1 / num_5

    print("El resultado de la operacion es:", result)
    print("El programa ha finalizado.")

# Si queremos para errores específico escribimos:
# except Tipo_de_Error_a_manejar
except ZeroDivisionError as error:
    print("Lo sentimos, no fue posible completar la operación.")
    print(error)

# Si queremos lidiar con más errores podemos agregar otro except
except NameError as error:
    print("Lo sentimos, la variable no se encuentra definida")

except IndexError as error:
    print("Lo sentimos, no es posible acceder a dicho índice")

# También podemos usar else para ejecutar algo sino hubo problemas
else: 
    print("El resultado de la operación es: ", result)

# Y si queremos ejecutar código independientemente si hubo error o no
# Usamos finally
finally:
    print("El programa ha finalizado")