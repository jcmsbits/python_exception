import logging
import traceback
import contextlib


logging.basicConfig(
    filename = "context_manager_logging.log",
    format = "%(asctime)s:%(levelname)s:%(message)s",
    level = logging.ERROR
)

# Para reducir código y no repetir el guardado de logs para cada error
# podemos usar el decorador @contextlib.contextmanager

@contextlib.contextmanager
def write_on_log_error():    
    try:
        # yield se va a cambiar por cualquier código que agreguemos 
        yield

    except Exception as error:
        exception_info = {
            "message" : str(error),
            "detail" : traceback.format_exc()
        }

        logging.error(exception_info)

with write_on_log_error():
    10 / 0