# pip install qrcode

# farklı bir interpreter kullanmak gerekebilir.

"""
import qrcode

code = qrcode.make("https://www.youtube.com")
code.save("qr1.png") # resim oluşturduk.

"""


import qrcode

code = qrcode.QRCode(
    version = 1, # 1 ile 40 arasında değerler alabilir.
    box_size = 100, # kutunun büyüklüğünü belirtiriz.
    border = 4 # sınırlarını belirleyebiliriz default olarak 4 gelir.   kenar boşluğu.
    
)

code.add_data("https://www.youtube.com")
code.make(fit = True) # kutuya tam oturabilsin diye fit = True dedik.
image = code.make_image(fill_color = "blue",back_color = "yellow") # arka plan vs değiştirdik. 
image.save("ilk.png")


