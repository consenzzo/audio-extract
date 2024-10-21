from moviepy.editor import *
from dotenv import load_dotenv
import os

load_dotenv()

caminho_video = os.getenv('CAMINHO_VIDEO')
caminho_audio = os.getenv('CAMINHO_AUDIO')

print(caminho_video)
# Carrega o vídeo .mov
video = VideoFileClip(caminho_video)

# Extrai o áudio do vídeo
audio = video.audio

# Salva o áudio como arquivo .mp3
audio.write_audiofile(caminho_audio)

# Fecha os objetos para liberar memória
audio.close()
video.close()
