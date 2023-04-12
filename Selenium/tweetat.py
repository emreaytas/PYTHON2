from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import json
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from random import randint

# ms Edge üzeriden calisacak... Edge sürümü = 112.0.1722.34  ....... x86 dosyası inerek bu .py dosaysının pathi üzerine getirilmelidir...

liste2 = []

email = "" # kullanici adi girilecek veya e posta str olarak...
password = "" # kullanci sifresi girilecek str olarak...
tweet = input("Atacaginiz tweeti giriniz: ")

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
        time.sleep(3)
        emailinput.send_keys(self.email,Keys.ENTER)
        time.sleep(3)
       
        time.sleep(3)
        passwordinput = self.driver.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        passwordinput.send_keys(self.password,Keys.ENTER)
        time.sleep(10)
        
    def tweetAt(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a").click()
        time.sleep(5)
        tweetinput = self.driver.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        time.sleep(3)
        tweetinput.send_keys(self.tweet)
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span").click()
        time.sleep(3)
        
        newTweet = input("Atacaginiz yeni tweeti giriniz(cikmak isterseniz q harfini giriniz): ")
        self.tweet = newTweet
        if self.tweet == "q":
            self.devam = False
            return
        self.zaman = datetime.now()
        self.tweet = f"- Tweet atilma zamani: {self.zaman.year}/{self.zaman.month}/{self.zaman.day} {self.zaman.hour}:{self.zaman.minute}:{self.zaman.second} --- {self.tweet}"
                   
        """
        //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div
        """        
        
        
twitter = Twitter(email,password,tweet)
       
twitter.SignIn()

while True:

    twitter.tweetAt()        
    if twitter.devam == False:
        print("Cikis yapiliyor...")
        time.sleep(1.5)
        break        
        
        
twitter.driver.close()



