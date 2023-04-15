
username = "emreaytas"
password = "34ffm72emre3436"
from selenium import webdriver
from selenium.webdriver.common.by import By #By ile neler üzerinden otomasyon çalışacak bulabiliriz...
from datetime import timedelta
import time
import json
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from random import randint

class Github():
    def __init__(self,username,password):
        self.url = "https://github.com"
        self.username = username
        self.password = password
        self.driver = webdriver.Edge()
        self.followers = []
                
    def signIN(self):
        self.driver.get(self.url+"/login")
        time.sleep(5)
        userinput = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/input[2]")
        userinput.send_keys(self.username)
        time.sleep(3)
        passwordinput = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]")
        passwordinput.send_keys(self.password)
        time.sleep(3)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[11]").click()
        time.sleep(3)
    
    def getFollowers(self):
        self.driver.get("https://github.com/"+self.username+"?tab=followers")
        time.sleep(2)
        
        if int(self.driver.find_element(By.CLASS_NAME,"text-bold color-fg-default")) <= 50:
            items = self.driver.find_elements(By.CSS_SELECTOR,".d-table table.fixed") #. ile css selector calisacak...
            for i in items:
                self.followers.append(i.find_element(By.CSS_SELECTOR,".link-gray.p1-1").text)
        else:
            
            while True:
                links =self.driver.find_element(By.CLASS_NAME,"BtnGroup").find_elements(By.TAG_NAME,"a")        
                if len(links) == 1:
                    if links[0].text == "Next":
                        links[0].click
                        time.sleep(3)
                        items = self.driver.find_elements(By.CSS_SELECTOR,".d-table table.fixed") #. ile css selector calisacak...
                    for i in items:
                        self.followers.append(i.find_element(By.CSS_SELECTOR,".link-gray.p1-1").text)
                
                    else:
                        break
                else:
                    for link in links:
                        if link.text == "Next":
                            link.click(1)
                            time.sleep(3)
                            items = self.driver.find_elements(By.CSS_SELECTOR,".d-table table.fixed") #. ile css selector calisacak...
                            for i in items:
                                self.followers.append(i.find_element(By.CSS_SELECTOR,".link-gray.p1-1").text)
                    break  
         

                 
github = Github(username,password)
github.signIN()
github.getFollowers()
a = 1
for i in github.followers:
    print(str(a)+"-"+i)
    