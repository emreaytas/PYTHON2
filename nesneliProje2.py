import threading # threading ile çağırırız...
import time

def start():
    print("Merhaba")
    time.sleep(2)
    print("selam")

start()

for i in range(10):
    t = threading.Thread(target=start)
    t.start()
    


