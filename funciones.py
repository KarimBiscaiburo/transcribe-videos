import os
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from datetime import datetime
from googletrans import Translator

idioma_video = "en" # [es: español, en: ingles]
idioma_traduccion = "es"

# Esta función se encarga de manejar el flujo del sistema
def ejecutar_funciones(url_video):
    # Transcripción del video original
    transcripcion = obtener_transcripcion(url_video)

    # Verificamos que no haya un error
    if "No se pudo obtener la transcripción" in transcripcion:
        print(transcripcion)
        return
    
    # Obtenemos la traducción
    traduccion = obtener_traduccion(transcripcion)
    
    # Verificamos que no haya un error
    if "No se pudo obtener la traduccion" in traduccion:
        print(traduccion)
        return
    
    # Fecha y hora para nombrar los archivos
    fecha_hora = obtener_fecha_hora_actual()
    
    nombre_archivo_trascripcion = f"{fecha_hora}_transcripcion.txt"
    nombre_archivo_traduccion = f"{fecha_hora}_traduccion.txt"
    
    # Guardamos la transcripcion
    guardar_transcripcion(transcripcion, nombre_archivo_trascripcion)
    # Guardamos la traducción
    guardar_traduccion(traduccion, nombre_archivo_traduccion)

# Función para obtener el ID del video a partir de la URL
def obtener_id_video(url):
    yt = YouTube(url)
    return yt.video_id

# Función para descargar la transcripción
def obtener_transcripcion(url):
    video_id = obtener_id_video(url)
    
    try:
        # Obtener transcripción en el idioma seleccionado
        transcripcion = YouTubeTranscriptApi.get_transcript(video_id, languages=[idioma_video])
        texto = " ".join([x['text'] for x in transcripcion])
        
        return texto
    except Exception as e:
        return f"No se pudo obtener la transcripción: {e}"

# Función para traduccir la transcripción
def obtener_traduccion(texto: str):
    traductor = Translator()
    max_caracteres = 500
    
    traduccion_total = ""
    
    try:
        # Divide el texto en partes más pequeñas si excede el límite de caracteres
        partes = [texto[i:i + max_caracteres] for i in range(0, len(texto), max_caracteres)]
        
        for parte in partes:
            # Traducir cada parte
            traduccion_parte = traductor.translate(parte, dest=idioma_traduccion).text
            traduccion_total += traduccion_parte + " "
        
        return traduccion_total.strip()  # Devuelve la traducción completa sin espacios adicionales
    except Exception as e:
        return f"No se pudo obtener la traduccion: {e}"
    
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
    
# Función para guardar en un archivo la traducción
def guardar_traduccion(texto, nombre_archivo, directorio="traducciones"):
    
    # Crear directorio si no existe
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    # Ruta completa del archivo
    ruta_archivo = os.path.join(directorio, nombre_archivo)
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    
    print(f"Traducción guardada en: {ruta_archivo}")

def obtener_fecha_hora_actual():
    # Obtiene la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # Formatea el día, mes y hora
    dia = fecha_hora_actual.strftime("%d")   # Día en formato de dos dígitos
    mes = fecha_hora_actual.strftime("%m")   # Mes en formato de dos dígitos
    hora = fecha_hora_actual.strftime("%H_%M_%S")  # Hora en formato de 24 horas

    return f"{dia}-{mes}-{hora}"