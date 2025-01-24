from contextlib import suppress
import logging

# Si queremos suprimir o silenciar los errores podemos usar 
# supress de contextlib o simplemente poner un pass en Exception (por ejemplo)

try:
    10 / 0

except Exception as error:
    pass


with suppress(Exception):
    10 / 0 