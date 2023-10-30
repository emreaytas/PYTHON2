
import platform
import psutil

def get_cpu_temperature():
    if platform.system() == "Windows":
        # Windows işletim sistemi için işlemci sıcaklığına erişim yok.
        return None
    elif platform.system() == "Linux":
        # Linux işletim sistemi üzerinde işlemci sıcaklığını oku
        try:
            temperature = psutil.sensors_temperatures()['coretemp'][0].current
            return temperature
        except:
            return None
    else:
        return None

temperature = get_cpu_temperature()

if temperature is not None:
    print(f"İşlemci Sıcaklığı: {temperature} °C")
else:
    print("İşlemci sıcaklığına erişim mümkün değil veya desteklenmiyor.")