import logging

# Para guardar los mensajes con logging usamos filename en basiconfig

logging.basicConfig(
    level = logging.ERROR,
    filename = "errors.log" # a
    )

try:
    10 / 0

except Exception as error:
    logging.error("Lo sentimos, no es posible completar la operación")
