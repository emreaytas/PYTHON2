# pip install speechrecognition
# pip install pyttsx3
# pip install pyaudio

# farklı bir interpreter kullanmak gerekebilir.

import speech_recognition
import pyttsx3
import pyaudio

recog1 = speech_recognition.Recognizer() # bir nesnemiz olacak. 

while True:
    
    try:
        with speech_recognition.Microphone() as mic:
            recog1.adjust_for_ambient_noise(mic,duration=0.2) # 0.2 saniye sonra dinleme duracak çalışmadan sonra.
            audio = recog1.listen(mic)
            text = recog1.recognize_google(audio)
            text = text.lower()
            print(f"Recognized: {text}")     
    except speech_recognition.UnknownValueError():
        recog1 = speech_recognition.Recognizer()
        continue
        


