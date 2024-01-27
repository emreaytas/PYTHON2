import subprocess # import ettik...
metadata = subprocess.check_output(['netsh','wlan','show','profiles'])
data = metadata.decode('utf-8',errors="backslashreplace")
data = data.split("\n")
profiles = []

for i in data:
    if "All User Profile" in i:
        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        profiles.append(i)

#print("{:<30}| {:<}".format("Wi-fi Name, Password"))
print("{:<30}| {:<}".format('WİFİ NAME','PASSWORD'))
print("-----------------------------------------------------------")
for i in profiles:
    try:
        
        results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear'])
        results = results.decode('utf-8',errors="backslashreplace")
        results = results.split("\n")
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b] 
        
        try:
            print("{:<30}| {:<}".format(i,results[0]))


        except IndexError:
            print("{:<30}| {:<}".format(i,""))
        
        
    except subprocess.CalledProcessError:
        print("HATA VAR...")
        
import time
time.sleep(10) 
input("ENTERA BASARSANIZ KAPANACAK...") 
      
        
