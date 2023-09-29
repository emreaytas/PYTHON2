# pip install speedtest-clip,pip uninstall speedtest-cli   
# ilede silebiliriz genel olaral pip uninstall paketadı ile silme yapabiliriz...
import speedtest # interpreter ile alakalı sorun yaşadık ama değiştirince sorun ortadan kalktı.
from time import sleep

s = speedtest.Speedtest() # objeyi oluşturduk. içindeki metotları kullanacağız.
print("Server list loading..")
sleep(0.5)
s.get_servers() # serverlari getirir.
print("....")
best_servers = s.get_best_server()
# print(best_servers)   # {'url': 'http://speedtest.awmbilisim.com:8080/speedtest/upload.php', 'lat': '41.0136', 'lon': '28.9550', 'name': 'Istanbul', 'country': 'Türkiye', 'cc': 'TR', 'sponsor': 'Awm Bilisim Hizmetleri', 'id': '44822', 'host': 'speedtest.awmbilisim.com:8080', 'd': 76.48079780734305, 'latency': 33.043}        
   #bir dict döner key value ilişkisi ile değerlere ulaşabiliriz.
print(f"Secilen server:{best_servers['host']} Ulke:{best_servers['country']}")
sleep(0.5)
print("Download testing...")
download = s.download()
print("Uploading testing")
sleep(0.5)
upload = s.upload()
print("Ping testing...")
ping = s.results.ping
sleep(0.5)

print("Download: "+str(download / (1024 * 1024))+" mb")
print("Upload: "+str(upload / (1024 * 1024))+ " mb") # bit olarak indiği için biz çeviririz. kaç mb indiririz görebiliriz.
print("Ping: "+str(ping)+" ms")




