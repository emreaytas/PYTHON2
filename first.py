website = "https://www.sadikturan.com"
website1 = website
course = "Python kursu: Bastan sona python programlama rehberiniz (40 saat)"
print("course karakter dizisi uzunlugu: "+str(len(course)))


print(website1)
print(course[:15]+"..."+course[len(course) - 16 : len(course) - 1])        
print(course[len(course) - 1::-1])

name,surname,age,job = "emre","aytas",20,"job"
print(f"Benim adim {name} {surname}, yasim {age} meslegim: {job}")
