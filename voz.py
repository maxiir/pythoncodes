from gtts import gTTS

texto='hola'
idioma='es'

audio=gTTS(text=texto,lang=idioma,show=False)

audio.save('audio.mp3')