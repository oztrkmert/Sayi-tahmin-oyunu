import random

hak = 5
sayi = random.randint(1,101)

print("1 ile 100 arasinda bir sayi tuttum! Bakalim tahmin edebilecek misin? Dikkatli ol sadece 5 hakka sahipsin.")

while hak > 0:
    tahmin = int(input("Tahminin nedir? "))

    if tahmin != sayi and tahmin > sayi:
        hak -= 1
        print(f"Yanlis tahmin. Daha kucuk sayilar dene. Kalan hak {hak}")
    elif tahmin != sayi and tahmin < sayi:
        hak -= 1
        print(f"Yanlis tahmin. Daha buyuk sayilar dene. Kalan hak {hak}")
    elif tahmin == sayi:
        print("Tebrikler! Sayiyi dogru tahmin ettin.")
        break
        
    if hak == 0:
        print("Hakkiniz bitti. Tuttugum sayi:", sayi)

print("Tekrar oynamak ister misin?")