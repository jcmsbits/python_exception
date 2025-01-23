# El traceback nos da un seguimiendo de donde salió el error
# para poder debuguear más rápido

# Para trabjar con la excepciones con Python obligatoriamente
# vamos a tener que trabajar con dos bloques Try - Except

# En Try ponemos el código que puede dar error
# Y en Except lo que queremos que se ejecute si da el error

try:
    num_1 = 10
    num_2 = 0
    num_3 = 3

    # result = num_1 / num_2
    result = num_1 / num_3

    print("El resultado de la operacion es:", result)
    print("El programa ha finalizado.")

# Si queremos para errores específico escribimos:
# except Tipo_de_Error_a_manejar
except ZeroDivisionError as error:
    print("Lo sentimos, no fue posible completar la operación.")
    print(error)

# También podemos usar else para ejecutar algo sino hubo problemas
else: 
    print("El resultado de la operación es: ", result)

# Y si queremos ejecutar código independientemente si hubo error o no
# Usamos finally
finally:
    print("El programa ha finalizado")