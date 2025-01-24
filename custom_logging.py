import logging
import traceback

logging.basicConfig(
    level = logging.ERROR,
    filename = "custom_error.log",
    format = "%(asctime)s:%(levelname)s:%(message)s"
)

try:
    10 / 0

except Exception as error:
    exception_info = {
        "message" : str(error),
        # traceback por defecto se activa solo sino usamos try y except
        # entonces tenemos usar format_exc
        "detail" : traceback.format_exc()
    }
    logging.error(exception_info)

