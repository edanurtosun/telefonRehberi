from kayit import Kayit
from adresdefteri import AdresDefteri
from kullanici import Kullanici

kullanicilar = []

a_d = AdresDefteri

kayit = Kayit

secim = None
kontrol = True

while kontrol:
    print("""
    #TELEFON REHBERİ#
    1. Kayit
    2. Giris
    3. Cikis
    """)
    secim = int(input("Seciminiz : "))

    kayit_yapildi_mi = False

    if secim == 1:  # kayit
        """Giris Ekranindasiniz . ."""

        kullanici_isim = input("Isminizi giriniz : ")
        kullanici_parola = int(input("Parolanizi giriniz : "))
        kisi = {
            'isim': kullanici_isim,
            'parola': kullanici_parola
        }
        kullanicilar.append(kisi)
        print("Kaydiniz basariyla gerceklestirilmistir")
        print(kullanicilar)
        print("*******")



    elif secim == 2:  # giris
        """Giris ekranindasiniz"""
        isim = input("Isminiz : ")
        parola = int(input("Parolaniz : "))
        for i in range(0,len(kullanicilar)):
            if kullanicilar[i]:
                while True:

                    print("""
                    1.Adres defteri olustur
                    2.Deftere kayit ekle
                    3.Kayit sil
                    4.Adres defteri sil
                    5.Cikis
                    """)

                    kullanici_secim = int(input("Seciminiz : "))

                    if kullanici_secim == 1:
                        print("~~~~Adres defteri olusturme")
                        defter_isim = input("Adres defterinin ismini giriniz : ")
                        olusturuldu_mu = a_d.__init__(a_d, defter_isim)
                        if olusturuldu_mu == True:
                            print("Adres defteri olusturuldu")
                        else:
                            print("Adres defteri olusturulamadi")

                    elif kullanici_secim == 2:
                        print("~~~~Adres defterine kayit ekle")
                        adres_defterinin_adi = input("Kayit eklemek istediginiz adres defterinin adini giriniz : ")
                        kayit_isim = input("Kayit edilecek kisinin adini giriniz : ")
                        kayit_soyisim = input("Kayit edilecek kisinin soyadini giriniz : ")
                        kayit_tel = input("Kayit edilecek kisinin telefon numarasini giriniz : ")

                        kayit_edildi_mi = kayit.__init__(kayit,adres_defterinin_adi,kayit_isim,kayit_soyisim,kayit_tel)
                        if kayit_edildi_mi == True:
                            print("Kayit adres defterine eklendi")
                        else:
                            print("Kayit yapilamadi")

                    elif kullanici_secim == 3:
                        pass

                    elif kullanici_secim == 4:
                        pass

                    elif kullanici_secim == 5:
                        break

                    else:
                        print("Yanlis secim yaptiniz")
            else:
                print("Giris yapilamadi")


        else:
            break

    elif secim == 3:  # cikis
        kontrol = False
    else:
        pass










































#
#
# kayit_yapilacak_kullanici = Kayit() #listeye kayit eklemek icin olusturuldu
# adres_defteri = AdresDefteri()
# kayit_var_mi = Kayit()
# kaydi_silinecek_kullanici = Kayit() # silinecek kayit icin olusturuldu
# kayit_yapildi_mi = False
#
# def kayit_yap(i, p, t, m):
#     a = kayit_yapilacak_kullanici.kayit_ekle(i, p, t, m)
#     if a == True:
#         return True
#     else:
#         return False
#
#
# def adres_defteri_olustur():
#     x = adres_defteri.adres_defteri_olustur()
#     if x == True:
#         return True
#     else:
#         return False
#
# def defter_kayit(k,i,t,m):
#     x = adres_defteri.deftere_kayit_ekle(k,i,t,m)
#     if x == True:
#         return True
#     else:
#         return False
#
#
# kontrol = True
#
# while kontrol:
#     print("""
#     #TELEFON REHBERİ#
#     1. Kayit
#     2. Giris
#     3. Cikis
#     """)
#     secim = int(input("Seciminiz : "))
#     kayit_yapildi_mi = False
#     if secim == 1:  # kayit
#         while kayit_yapildi_mi == False:
#             print("Kayit ekranina giris yaptiniz")
#             kullanici_isim = input("Kullanici adinizi giriniz : ")
#             kullanici_parola = input("Kullanici parolanizi giriniz : ")
#             kullanici_tel = int(input("Telefon numaranizi giriniz : "))
#             kullanici_e_posta = input("E-posta adresinizi giriniz : ")
#
#             kayit_tamamlandi_mi = kayit_yap(kullanici_isim, kullanici_parola, kullanici_tel, kullanici_e_posta)
#
#             if kayit_tamamlandi_mi is True:
#                 print("Kaydiniz yapilmistir")
#                 kayit_yapildi_mi = True
#             else:
#                 print("Girdiginiz bilgiler hatali")
#                 break
#
#     elif secim == 2:  # giris
#         print("Giris ekranindasiniz")
#         isim = input("Isminiz : ")
#         parola = input("Parolaniz : ")
#
#         k = kayit_var_mi.kayit_kontrol(isim,parola)
#
#         if k == True:
#             print("Girisiniz basariliyla gerceklestirildi")
#         # if isim == "eda" and parola == "1":
#             print("""
#             1.Adres defteri olustur
#             2.Deftere kayit ekle
#             3.Kayit sil
#             4.Adres defteri sil
#             5.Cikis
#             """)
#             kullanici_secim = int(input("Seciminiz : "))
#
#             if kullanici_secim == 1:
#                 print("Adres defteri olusturma")
#
#                 sonuc = adres_defteri_olustur()
#                 if sonuc == True:
#                     print("Adres defteri olusturuldu")
#                 else:
#                     print("Defter olusturulamdi")
#             elif kullanici_secim == 2:
#                 print("Deftere kayit ekleme")
#                 kategori = input("Kategori : ")
#                 isim = input("Isim : ")
#                 tel = input("Tel : ")
#                 mail = input("E-posta : ")
#                 s = defter_kayit(kategori,isim,tel,mail)
#                 if s == True:
#                     print("Kayit olusturuldu")
#                 else:
#                     print("Kayit olusturulamdi")
#             elif kullanici_secim == 3:
#                 print("kayitli kullanicilar")
#                 print(kayitli_kullanici_mi.kayitli_kullanicilar())
#                 silinecek_isim = input("Silmek istediginiz kaydin ismini giriniz : ")
#                 silindi_mi = kaydi_silinecek_kullanici.kayit_sil(silinecek_isim)
#                 if silindi_mi == True:
#                     print("Kayit silinmistir")
#                 else:
#                     print("Kayit silinemedi")
#             elif kullanici_secim == 4:
#                 print("Adres defteri sil")
#                 adres_defteri.adres_defteri()
#                 silinecek_kategori = input("Silmek istediğiniz adres defterinin kategorisini giriniz : ")
#                 sonuc = adres_defteri.adres_defteri_sil(silinecek_kategori)
#                 if sonuc == True:
#                     print("Defter silindi")
#                 else:
#                     print("Defter silinemedi")
#             elif kullanici_secim == 5:
#                 break
#             else:
#                 print("Yanlis secim yaptiniz")
#         else:
#             break
#
#     elif secim == 3:  # cikis
#         kontrol = False
#     else:
#         pass
#
# print("Program sonlandi")