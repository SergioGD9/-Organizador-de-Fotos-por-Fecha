# Organizador de Fotos por Fecha

Este script de Python ayuda a organizar automáticamente tus fotos en carpetas según la fecha indicada en el nombre de cada archivo. Es útil para ordenar grandes cantidades de fotos descargadas o desorganizadas, especialmente aquellas con nombres que siguen patrones de fechas.

### Funcionamiento

El script lee todos los archivos de un directorio específico que contienen fotos. Extrae las fechas de los nombres de los archivos asumiendo un formato de fecha común como "YYYYMMDD" o "YYYY-MM-DD". Luego, crea carpetas para cada fecha única y mueve las fotos a la carpeta correspondiente.

### Estructura de Nombres Aceptada

El script funciona asumiendo que el nombre de las fotos contiene fechas en los siguientes formatos:

+ "YYYYMMDD" (Ejemplo: 20230102 para el 2 de Enero de 2023).
+ "YYYY-MM-DD" (Ejemplo: 2023-01-02 para el 2 de Enero de 2023).
  

### Instrucciones de Uso

1. Instalar Python: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org.
2. Configurar el Script: Cambia la variable path_to_photos en el script al directorio donde tienes almacenadas tus fotos.
3. Ejecutar el Script: Guarda el script en un archivo .py y ejecútalo desde tu terminal o línea de comandos.
   

### Ejemplo de Uso

1. Descarga y guarda tus fotos en una carpeta específica.
2. Copia el script en el mismo directorio donde está la carpeta de las fotos o asegúrate de que la ruta en el script apunta al lugar correcto.
3. Ejecuta el script. Las fotos serán organizadas en carpetas por fecha.
   
### Notas Adicionales

+ Si el script se ejecuta múltiples veces o se añaden más fotos, aquellas con fechas que ya tienen una carpeta asignada serán movidas a las carpetas existentes sin duplicar o sobreponer los datos.
+ Asegúrate de que los nombres de las fotos sigan los patrones de fecha que el script está programado para reconocer. Si tus fotos tienen un formato de fecha diferente, necesitarás modificar la expresión regular en el script para adaptarse a tu formato.
  

### Licencia

Este script es de dominio público. Siéntete libre de modificarlo y redistribuirlo según tus necesidades.

