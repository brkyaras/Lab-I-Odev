def k_kucuk(k, liste):
    if k < 1 or k > len(liste):
        return "Geçersiz sıra numarası"

    tekrar_edenler = []
    for eleman in liste:
        if eleman not in tekrar_edenler:
            tekrar_edenler.append(eleman)

    tekrar_edenler.sort()

    k_kucuk_eleman = tekrar_edenler[k - 1]

    return k_kucuk_eleman


def en_yakin_cift(hedef, liste):
    if not liste:
        return "Liste boş."

    en_kucuk_fark = float('inf')
    en_yakin_ikili = None

    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            toplam = liste[i] + liste[j]
            fark = abs(hedef - toplam)

            if fark < en_kucuk_fark:
                en_kucuk_fark = fark
                en_yakin_ikili = (liste[i], liste[j])

    return en_yakin_ikili


def tekrar_eden_elemanlar(liste):
    tekrar_edenler = []

    for eleman in liste:
        if liste.count(eleman) > 1 and eleman not in tekrar_edenler:
            tekrar_edenler.append(eleman)

    return tekrar_edenler


def matris_olustur():
    try:
        satir_sayisi = int(input("Matrisin satır sayısını girin: "))
        sutun_sayisi = int(input("Matrisin sütun sayısını girin:"))

        matris = []
        for i in range(satir_sayisi):
            satir = []
            for j in range(sutun_sayisi):
                deger = float(input(f"Matrisin [{i + 1}][{j + 1}] elemanını girin: "))
                satir.append(deger)
            matris.append(satir)

        return matris
    except ValueError:
        print("Geçersiz bir değer girdiniz. Lütfen sayıları kullanın.")


def matris_carpimi(matris1, matris2):
    satir1 = len(matris1)
    sutun1 = len(matris1[0])
    satir2 = len(matris2)
    sutun2 = len(matris2[0])

    if sutun1 != satir2:
        return "Matrisler çarpılamaz."

    sonuc = [[0 for _ in range(sutun2)] for _ in range(satir1)]

    for i in range(satir1):
        for j in range(sutun2):
            for k in range(sutun1):
                sonuc[i][j] += matris1[i][k] * matris2[k][j]

    return sonuc


def kelime_frekansi(text_dosya_yolu):
    try:
        with open(text_dosya_yolu, 'r', encoding='utf-8') as dosya:
            metin = dosya.read()

        kelimeler = metin.lower().split()

        frekanslar = {}
        for kelime in kelimeler:
            if kelime in frekanslar:
                frekanslar[kelime] += 1
            else:
                frekanslar[kelime] = 1

        return frekanslar

    except FileNotFoundError:
        return "Dosya bulunamadı."
    except Exception as e:
        return f"Hata oluştu: {e}"


def en_kucuk_degeri_bul():
    try:
        liste = input("Listeyi virgülle ayırarak girin: ").split(",")
        liste = [int(x) for x in liste]

        if not liste:
            print("Liste boş.")
            return

        en_kucuk = liste[0]

        for eleman in liste:
            if eleman < en_kucuk:
                en_kucuk = eleman

        print(f"En küçük değer: {en_kucuk}")
    except ValueError:
        print("Geçersiz bir değer girdiniz. Lütfen sayıları kullanın.")


def karekok_hesapla(N, x0, tol=1e-10, maxiter=10):
    x = x0
    for iterasyon in range(maxiter):
        x_sonraki = 0.5 * (x + N / x)
        hata = abs(x_sonraki ** 2 - N)

        if hata < tol:
            return x_sonraki
        x = x_sonraki

    secim = input(
        f"{maxiter} iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirmek ister misiniz? ("
        f"evet:e / hayır: h): ")
    if secim.lower() == 'e':
        maxiter = int(input("Yeni maxiter değerini girin: "))
        return karekok_hesapla(N, x0, tol, maxiter)
    else:
        return x


def eb_ortak_bolen(sayi1, sayi2):
    while sayi2 != 0:
        sayi1, sayi2 = sayi2, sayi1 % sayi2
    return sayi1


def asal_veya_degil(sayi):
    if sayi <= 1:
        return f"{sayi} bir asal sayı değildir."
    for i in range(2, sayi):
        if sayi % i == 0:
            return f"{sayi} bir asal sayı değildir."
    return f"{sayi} bir asal sayıdır."


def hizlandirici(n, k, fib_k, fib_k1):
    if n == k:
        return fib_k
    else:
        return hizlandirici(n, k + 1, fib_k + fib_k1, fib_k)


def hizlandirilmis_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return hizlandirici(n, 1, 1, 0)


def menu():
    while True:
        print("1. k'nıncı En Küçük Elemanı Bul")
        print("2. En Yakın Çifti Bul")
        print("3. Tekrar Eden Elemanları Bul")
        print("4. Matris Çarpımı")
        print("5. Kelime Frekanslarını Hesapla")
        print("6. En Küçük Değeri Bul")
        print("7. Karekök Hesapla")
        print("8. Ebob Bul")
        print("9. Asal Sayı Kontrolü")
        print("10. Fibonacci Sayısını Hesapla")
        print("11. Çıkış")
        secim = input("Seçiminizi yapın: ")
        print()

        if secim == '1':
            liste = input("Listeyi virgülle ayırarak girin: ").split(",")
            liste = [int(x) for x in liste]
            k = int(input("k değerini girin: "))
            sonuc = k_kucuk(k, liste)
            print(f"{k}'ıncı en küçük eleman: {sonuc}\n")

        elif secim == '2':
            hedef = int(input("Hedef sayıyı girin: "))
            liste = input("Listeyi virgülle ayırarak girin: ").split(",")
            liste = [int(x) for x in liste]
            sonuc = en_yakin_cift(hedef, liste)
            print(f"En yakın çift: {sonuc[0]} ve {sonuc[1]}\n")

        elif secim == '3':
            liste = input("Listeyi virgülle ayırarak girin: ").split(",")
            liste = [int(x) for x in liste]
            sonuc = tekrar_eden_elemanlar(liste)
            print("Tekrar eden elemanlar:")
            for eleman in sonuc:
                print(eleman, end=" ")
            print("\n")

        elif secim == '4':
            print("Birinci Matris:")
            matris1 = matris_olustur()
            print()
            print("İkinci Matris:")
            matris2 = matris_olustur()
            sonuc = matris_carpimi(matris1, matris2)
            print()
            print("Çarpım Sonucu:")
            for satir in sonuc:
                for eleman in satir:
                    print(eleman, end=" ")
                print()
            print()

        elif secim == '5':
            dosya_yolu = input("Text dosyasının yolunu girin: ")
            sonuc = kelime_frekansi(dosya_yolu)
            for kelime, frekans in sonuc.items():
                print(f"{kelime}: {frekans}")
            print()

        elif secim == '6':
            en_kucuk_degeri_bul()
            print()

        elif secim == '7':
            N = float(input("Karekökü alınacak sayıyı girin: "))
            x0 = float(input("İlk tahmin değerini girin: "))
            sonuc = karekok_hesapla(N, x0)
            print("Sonuç:", sonuc)
            print()

        elif secim == '8':
            sayi1 = int(input("Birinci tam sayıyı girin: "))
            sayi2 = int(input("İkinci tam sayıyı girin: "))
            ebob = eb_ortak_bolen(sayi1, sayi2)
            print(f"{sayi1} ve {sayi2} sayılarının en büyük ortak böleni (EBOB): {ebob}\n")

        elif secim == '9':
            sayi = int(input("Bir sayı girin: "))
            sonuc = asal_veya_degil(sayi)
            print(sonuc)
            print()

        elif secim == '10':
            n = int(
                input("Fibonacci dizisinde hangi sıradaki sayıyı hesaplamak istersiniz? Bir pozitif tam sayı girin: "))
            if n < 0:
                print("Negatif bir sayı girdiniz. Lütfen pozitif bir tam sayı girin.")
            else:
                sonuc = hizlandirilmis_fibonacci(n)
                print(f"Fib({n}) = {sonuc}")
                print()

        elif secim == '11':
            print("Programdan çıkılıyor.")
            break

        else:
            print("Geçersiz seçenek! Lütfen 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 veya 11 girin.\n")


menu()
