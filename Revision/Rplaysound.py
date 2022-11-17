from gtts import *
from playsound import *
# text=("jai shree ram,jai shree ram,jai shree ram,jai shree ram,jai shree ram")
# audio=gTTS(text)
# audio.save("jaighosh.mp3")
# playsound("jaighosh.mp3")
# print("jai shree ram")

def play_sound():
    text = ("jai shree ram,jai shree ram")
    audio = gTTS(text)
    audio.save("jaighosh.mp3")
    playsound("jaighosh.mp3")
    print("jai shree ram")
play_sound()








