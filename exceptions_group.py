from exceptions import CustomError_1Exception, CustomError_2Exception, CustomError_3Exception


try:
    # Python 3.11
    raise ExceptionGroup(
        "Un grupo de errores propios",
        [CustomError_1Exception(), CustomError_2Exception(), CustomError_3Exception()]
    )

# except ExceptionGroup as group:
#     print("Error de grupo", group)

# Podemos ejecutar las excepciones independientes del grupo
except *CustomError_1Exception:
    print("Error de tipo 1")

except *CustomError_2Exception:
    print("Error de tipo 2")

except *CustomError_3Exception:
    print("Error de tipo 3")
