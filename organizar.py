"""
Organizador de Fotos por Fecha

Este script organiza automáticamente las fotos en carpetas basadas en la fecha indicada en su nombre.

Creado por: SergioGD9 (https://github.com/SergioGD9)
Por favor, siéntete libre de utilizar y modificar este script según tus necesidades. Si encuentras este script útil,
considera mencionar o agradecer al creador.

"""


import os
import re
import shutil

# Configura la ruta al directorio donde están las fotos.
path_to_photos = 'tu/ruta/de/archivos'

# Cambia al directorio de las fotos.
os.chdir(path_to_photos)

# Lista todos los archivos en el directorio.
files = os.listdir()

for file in files:
    # Busca las fechas en el nombre del archivo usando expresiones regulares.
    match = re.search(r'(20\d{2})(-|)(\d{2})(-|)(\d{2})', file)
    if match:
        # Construye una cadena con la fecha.
        year, _, month, _, day = match.groups()
        date_folder = f"{year}-{month}-{day}"

        # Crea un directorio con la fecha como nombre si no existe.
        if not os.path.exists(date_folder):
            os.mkdir(date_folder)

        # Mueve el archivo a la carpeta correspondiente.
        shutil.move(file, os.path.join(date_folder, file))

print("Organización de fotos por fecha completada.")
