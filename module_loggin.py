import logging

# Con logging podemos hacer avisos de diferentes tipos de categoria

# INFO     = 10
# DEBUG    = 20
# WARNING  = 30
# ERROR    = 40
# CRITICAL = 50

# Por defecto logging solo muestra los mensaje que sean >= 30
# para cambiarlo usamos el método basiconfig

# Se puede modificar por la contante o por el numero
# logging.basicConfig(level = logging.INFO)
logging.basicConfig(level = 10)

logging.info("Hola, este es un mensaje informativo")
logging.debug("Hola, este es un mensaje para debug")
logging.warning("Hola, este es un mensaje de advertencia")
logging.error("Hola, este es un mensaje de error")
logging.critical("Hola, este es un mensaje CRITICO!!!!!!!!!")