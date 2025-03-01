import os

def ensure_directory_exists(directory: str):
    """
    Verifica si un directorio existe, si no, lo crea.

    :param directory: Ruta del directorio a verificar o crear.
    """
    os.makedirs(directory, exist_ok=True)
