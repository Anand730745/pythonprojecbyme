#google text to speech
from gtts import *
from playsound import*

text=("pushparaj sala jhukega nahi")
audio=gTTS(text)
audio.save('merageet.mp3')
playsound('merageet.mp3')

#print('audio generated')
