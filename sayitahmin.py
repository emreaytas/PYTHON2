from random import randint
sayi = randint(0,100)
for i in range(5):
    a = int(input("Sayinizi giriniz: "))
    if a == sayi:
        print("Sayiyi buldunuz...")
        break
    elif a < sayi:
        print("Sayi daha yukarida...")
    else:
        print("Sayi asagida.")

