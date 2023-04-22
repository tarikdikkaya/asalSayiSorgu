# Kullanıcıdan bir sayı girişi yapmasını istiyoruz.
girilenSayi = int(input("Asal olup olmadığını kontrol etmek istediğiniz sayıyı giriniz: "))

# Girilen sayıyı tam bölen sayıları kaydetmek için bir liste oluşturuyoruz.
bolunenler = []

while True:
    # Girilen sayının 2'den kendisine kadar bütün sayılara tek tek böldürüyoruz, 
    # tam bölünen sayıları 'bolunenler' listesine ekletiyoruz.
    for i in range (2,girilenSayi):
        if girilenSayi % i == 0:
            bolunenler.append(i)

    # 'bolunenler' listesinin uzunluğu 0'a eşit değilse yani sayının tam böleni varsa
    # kullanıcıya sayının asal olmadığını bildiriyoruz. 
    if len(bolunenler) != 0:
        print(f"{girilenSayi} asal değil. {bolunenler} sayılarına bölünüyor.")
        break
    
    # Eğer 'bolunenler' listesi 0'a eşit ise yani sayının tam böleni yoksa kullanıcıya 
    # sayının asal olduğunu bildiriyoruz.
    else:
        print(f"{girilenSayi} asal.")
        break
