# öncelikle bir mödül lazım python ile geldiği için bir şey yapmamıza gerek yok.
from smtplib import SMTP #mail göndermek için kullanılan bir mödül simple mail transfer protocol(SMTİ)

try:
    # mail mesaj bilgisi
    subject = "TEST" #konu bilgisi...
    message = input("Mesajinizi giriniz: ")
    content = f"Subject: {subject}\n{message}" # neden böyle yaptık bunun nedeni ise = normalde tek string olursa mesaj olarak algılar...

    # gönderen mailin hesap bilgileri...
    myMailAdress = "....@gmail.com"
    myPassword = "......" 

    # kime gönderilecek... hangi mail adresi...
    sendTo = ".....@...com"

    mail = SMTP("smtp.gmail.com",587) # eposta sunucusuna bağlantı işlemleri...  host adresi girmemiz lazım...   mesela yandex ile göndereceğiz o zaman imap yandex diyerek güncel ve resmi bilgilere ulaşabiliriz.
    mail.ehlo() # mail sunucusuna bağlanmak için gereken işlem.
    mail.starttls() # mesajları şifreli göndermek için kullanılır.
    mail.login(myMailAdress,myPassword) # mail sunucusunda oturum açmak için kullanılır.
    mail.sendmail(myMailAdress,sendTo,content.encode("utf_8"))
except Exception as e:
    print("Hata var")
    print(e)
    
    
# eğer gmail ile mail göndermek istersek o hesaptan biz Daha az güvenli uygulamalara izin veri'i açık hale getirmeliyiz. yoksa olmaz.