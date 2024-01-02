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
path_to_photos = r"C:\Users\sergi\Pictures\fotos y videos"

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
        
        # Define las carpetas de año y mes.
        year_folder = f"{year}"
        month_folder = f"{month}"

        # Crea un directorio para el año si no existe.
        if not os.path.exists(year_folder):
            os.mkdir(year_folder)

        # Construye la ruta al directorio del mes dentro del año.
        month_directory_path = os.path.join(year_folder, month_folder)

        # Crea un directorio para el mes si no existe.
        if not os.path.exists(month_directory_path):
            os.mkdir(month_directory_path)

        # Mueve el archivo a la carpeta correspondiente.
        shutil.move(file, os.path.join(month_directory_path, file))

print("Organización de fotos por año y mes completada.")
