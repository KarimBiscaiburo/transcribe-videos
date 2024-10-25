# DETALLES

Este pequeño código puede ser útil cuando necesites transcribir todo lo que hablan en un video.

>[!WARNING]
> Esto solo extrae la transcripción, no le da formato. Por lo que de requerirlo lo vas a tener que hacer manualmente.

## Funcionamiento

Deberas cambiar en "index.py" la url del video que quieras transcribir y en "funciones.py" el idioma en el que esté dicha transcripción de ser necesario.

Luego ejecuta el siguiente comando "py index.py" (procura estar ubicado en la raíz del proyecto).

Esto va a crear una carpeta "transcripciones" y dentro se guardaran todas las transcripciones que realices en archivos ".txt", con el nombre de "día-mes-hora_minutos_segundos"

## Dependencias

>[!TIP]
> Es recomendable crear un entorno virtual para instalar las dependencias, esto para no instalarlas globalmente en tu sistema y no generar posibles conflictos.
> * Para esto puedes ejecutar los siguientes comandos:
> 1. Crear entorno virtual: "python -m venv venv".
> 2. Activar el entorno: "venv/Scripts/activate (Windows) ; source venv/bin/activate (Linux/macOS)".

>[!WARNING]
> Es posible que dependiendo las restricciones del sistema que tengas configurada, tengas errores al crear el entorno virtual. Puedes ejecutar Powershell como administrador, ejecutar "Set-ExecutionPolicy RemoteSigned", activar el entorno virtual y por último ejecutar "Set-ExecutionPolicy Restricted".

>[!IMPORTANT]
> En el archivo "requirements.txt" vas a encontrar las dependencias necesarias que deberas instalar para que funcione.