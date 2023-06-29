import speech_recognition as sr
from pydub import AudioSegment
import os

# Ruta del archivo MP3
mp3_file = "millon.mp3"

# Ruta de salida para el archivo WAV
wav_file = "salida.wav"

# Convertir MP3 a WAV
audio = AudioSegment.from_mp3(mp3_file)
audio.export(wav_file, format="wav")

# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

# Transcribir el archivo WAV
with sr.AudioFile(wav_file) as source:
    # Leer el archivo de audio
    audio_data = r.record(source)
    # Realizar la transcripción utilizando el servicio de reconocimiento de voz
    text = r.recognize_google(audio_data, language="es-MX")

# Imprimir el texto transrito
print(text)
