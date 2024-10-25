import os
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from datetime import datetime

idioma = "en" # [es: español, en: ingles]

# Función para obtener el ID del video a partir de la URL
def obtener_id_video(url):
    yt = YouTube(url)
    return yt.video_id

# Función para descargar la transcripción
def obtener_transcripcion(url):
    video_id = obtener_id_video(url)
    
    try:
        # Obtener transcripción en el idioma seleccionado
        transcripcion = YouTubeTranscriptApi.get_transcript(video_id, languages=[idioma])
        texto = "\n".join([x['text'] for x in transcripcion])
        
        return texto
    except Exception as e:
        return f"No se pudo obtener la transcripción: {e}"

# Función para guardar en un archivo la transcripción
def guardar_transcripcion(texto, nombre_archivo, directorio="transcripciones"):
    
    # Crear el directorio si no existe
    if not os.path.exists(directorio):
        os.makedirs(directorio)
        
    # Ruta completa del archivo
    ruta_archivo = os.path.join(directorio, nombre_archivo)
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto)
        
    print(f"Transcripción guardada en: {ruta_archivo}")

def obtener_fecha_hora_actual():
    # Obtiene la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # Formatea el día, mes y hora
    dia = fecha_hora_actual.strftime("%d")   # Día en formato de dos dígitos
    mes = fecha_hora_actual.strftime("%m")   # Mes en formato de dos dígitos
    hora = fecha_hora_actual.strftime("%H_%M_%S")  # Hora en formato de 24 horas

    return f"{dia}-{mes}-{hora}"