from selenium import webdriver
import time
driver = webdriver.Edge()
url = "https://www.github.com"
driver.get(url) # tarayıcının çalışacağı url'yi belirledik...
time.sleep(10)
driver.maximize_window() # elde olan tarayıcıyı tam ekran yaptık...
driver.save_screenshot("newScreen.png") # ekran görüntüsü alıp sonra python dosyamıza ekledi...

url = "https://www.github.com/emreaytas"
driver.get(url) # driver'a yeni çalışma urlsini gönderdik...
print(driver.title) # başlık yazdırdık...
if "emreaytas" in driver.title:
    driver.save_screenshot("Ekranfotosu.png")
driver.back() # geri gitmemizi sağladı..

time.sleep(2)

driver.forward() # ileri gitmemizi sağladı...

print(driver.title) # bize sayfanın title kısmını getirir...
time.sleep(10)
driver.close() # pointerlar gibi driver'ı kapatarız çalışmasını bitiririz...




