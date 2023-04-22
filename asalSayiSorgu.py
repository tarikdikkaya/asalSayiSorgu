# Kullanıcıdan bir sayı girişi yapmasını istiyoruz.
girilenSayi = int(input("Asal olup olmadığını kontrol etmek istediğiniz sayıyı giriniz: "))

# Girilen sayıyı tam bölen sayıları kaydetmek için bir liste oluşturuyoruz.
bolenler = []

while True:
    # Girilen sayının 2'den kendisine kadar bütün sayılara tek tek böldürüyoruz, 
    # tam bölen sayıları 'bolenler' listesine ekletiyoruz.
    for i in range (2,girilenSayi):
        if girilenSayi % i == 0:
            bolenler.append(i)

    # 'bolenler' listesinin eleman sayısı 0'a eşit değilse yani sayının tam böleni varsa
    # kullanıcıya sayının asal olmadığını bildiriyoruz. 
    if len(bolenler) != 0:
        print(f"{girilenSayi} asal değil. {bolenler} sayılarına bölünüyor.")
        break
    
    # Eğer 'bolenler' listesinin eleman sayısı 0'a eşit ise yani sayının tam böleni yoksa kullanıcıya 
    # sayının asal olduğunu bildiriyoruz.
    else:
        print(f"{girilenSayi} asal.")
        break
