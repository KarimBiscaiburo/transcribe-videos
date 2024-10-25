from funciones import obtener_transcripcion, obtener_fecha_hora_actual, guardar_transcripcion

# Ejemplo de uso
url_video = "https://www.ejemplo.com"  # Reemplaza con la URL de tu video
transcripcion = obtener_transcripcion(url_video)

fecha_hora = obtener_fecha_hora_actual()
nombre_archivo = f"{fecha_hora}_transcripcion.txt"

if "No se pudo obtener la transcripción" not in transcripcion:
    guardar_transcripcion(transcripcion, nombre_archivo)
else:
    print(transcripcion)
