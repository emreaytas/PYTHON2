from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import timedelta
import time
import json
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from random import randint

# ms Edge üzeriden calisacak... Edge sürümü = 112.0.1722.34  ....... x86 dosyası inerek bu .py dosaysının pathi üzerine getirilmelidir...



email = "" # kullanici adi girilecek veya e posta str olarak...
password = "" # kullanci sifresi girilecek str olarak...
gitmezamani = datetime(2023,5,15,0,0,0)
zaman1 = datetime.now()
fark = gitmezamani - zaman1
tweet = f"AKP'nin gitmesine: {int(int(fark.days) / 30)} AY {(int(fark.days) % 30)} GUN {int(int(fark.seconds) / 3600)} SAAT { (int (int(fark.seconds) / 60) - ((int(int(fark.seconds) / 3600)) * 60))} DAKIKA {(int(fark.seconds) % 60)} SANIYE KALDI!!!"

class Twitter():
    def __init__(self,email,password,tweet):
        self.devam = True
        self.driver = webdriver.Edge()
        self.email = email
        self.password = password
        self.zaman = datetime.now()
        self.tweet = f"- Tweet atilma zamani: {self.zaman.year}/{self.zaman.month}/{self.zaman.day} {self.zaman.hour}:{self.zaman.minute}:{self.zaman.second} --- {tweet}"
    
    def SignIn(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10)
        self.driver.maximize_window()
        
        emailinput = self.driver.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")               
        time.sleep(2)
        emailinput.send_keys(self.email,Keys.ENTER)
        time.sleep(2)
       
        time.sleep(2)
        passwordinput = self.driver.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        passwordinput.send_keys(self.password,Keys.ENTER)
        time.sleep(4)
        
    def tweetAt(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a").click()
        time.sleep(2)
        tweetinput = self.driver.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        time.sleep(2)
        tweetinput.send_keys(self.tweet)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span").click()
        time.sleep(2)
        
        gitmezamani = datetime(2023,5,15,0,0,0)
        zaman1 = datetime.now()
        fark = gitmezamani - zaman1
        newTweet = f"AKP'nin gitmesine: {int(int(fark.days) / 30)} AY {(int(fark.days) % 30)} GUN {int(int(fark.seconds) / 3600)} SAAT { (int (int(fark.seconds) / 60) - ((int(int(fark.seconds) / 3600)) * 60))} DAKIKA {(int(fark.seconds) % 60)} SANIYE KALDI!!!"
        self.tweet = newTweet
        if self.tweet == "q":
            self.devam = False
            return
        self.zaman = datetime.now()
        self.tweet = f"- Tweet atilma zamani: {self.zaman.year}/{self.zaman.month}/{self.zaman.day} {self.zaman.hour}:{self.zaman.minute}:{self.zaman.second} --- {self.tweet}"
                   
        """
        //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div
        """        
        time.sleep(1)
        
twitter = Twitter(email,password,tweet)
       
twitter.SignIn()

while True:

    twitter.tweetAt()        
    if twitter.devam == False:
        print("Cikis yapiliyor...")
        time.sleep(1.5)
        break        
        
        
twitter.driver.close()



