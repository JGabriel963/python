from gtts import gTTS
from playsound import playsound

def create_audio(message: str):
    tts = gTTS(message, lang='pt-br')
    tts.save('message.mp3')
    playsound('message.mp3')

# 2 - Utilização da função diretamente
# create_audio("Olá, mundo! Espero me desenvolver muito com Python")

# 3 - Utilização da função via Input
sentence = input("Digite a frase a ser falada:\n")
create_audio(sentence)