import numpy as np;import pandas as pd
import cv2  # pip install opencv-python ile yükleme yaparız eğer hata verir select different printer ile python yorumlayıcısını değiştirebiliriz...
import mediapipe as mp  # pip install mediapipe
import math
import VolumeProjectModule as vpm


wCam,hCam = 640,480 # default height ve weight değişkenler... ekranın büyüklüğünü belirleriz...
mycap =  cv2.VideoCapture(0)  # dahili camı kullandık. harici ise 1,2 vs vs diye seçebiliriz.
mycap.set(3,wCam) # burada boyut ayarlamalarını yaptık 
mycap.set(4,hCam)

detector = vpm.handDetector() # yüzde 70 oran verdik.
print("hello")
while True:
    success,img = mycap.read()
    img = detector.findHands(img)
    cv2.imshow("img",img)
    cv2.waitKey(1)
    
    
