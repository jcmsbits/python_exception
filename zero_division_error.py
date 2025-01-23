# El traceback nos da un seguimiendo de donde salió el error
# para poder debuguear más rápido

# Para trabjar con la excepciones con Python obligatoriamente
# vamos a tener que trabajar con dos bloques Try - Except

# En Try ponemos el código que puede dar error
# Y en Except lo que queremos que se ejecute si da el error

num_1 = 10
num_2 = 0

result = num_1 / num_2

print("El resultado de la operacion es:", result)
print("El programa ha finalizado.")