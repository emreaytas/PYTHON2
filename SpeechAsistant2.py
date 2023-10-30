# pip install SpeechRecognition

# pip install gTTS (metini sese çevirir.)
# pip install playsound

import speech_recognition as SR
import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random 
import os

"""

r = SR.Recognizer()

with SR.Microphone() as source:
    audio = r.listen(source)
    voice = r.recognize_google(audio,language="tr-TR") # türkçeye çeviririz default olarak ingilizce dinler.
    print(voice)

"""

def speech(string):
    tts = gTTS(string,lang="tr") # dil belirleyebiliriz.
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

r = SR.Recognizer()
def record(ask = False): # default olarak False verdik.
    
    if ask:
        speech(ask)
    
    with SR.Microphone() as source:
        audio = r.listen(source)
        voice = ""
        try:
            
            voice = r.recognize_google(audio,language="tr-TR") # türkçeye çeviririz default olarak ingilizce dinler.
        
        except SR.UnknownValueError:
            speech("Anlayamadim.")
        except SR.RequestError:
            speech("Sistem calismiyor.")    
            
        return voice




def response(voice):
    if "nasılsın" in voice:
        speech("iyi senden.")
    if "saat kaç" in voice:
        speech(datetime.datetime.now().strftime("%H:%M:%S"))
    if "arama yap" in voice:
        search = record("ne aramak istiyorsun")
        url = "https://google.com/search?q= " + search        
        webbrowser.get().open(url) 
        speech(search + " icin bulduklarım")
    if "tamamdır" in voice:
        speech("Gorusuruz.")
        exit()


    
        
print("Nasil yardimci olabilirim.")
time.sleep(1)
while True:
    
    voice = record()
    response(voice)



    