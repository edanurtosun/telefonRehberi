import uuid
# kullanicilar = list()

adresDefteri = []
kullanicilar = []

class Kullanici:

    def __init__(self,isim ,parola):
        self.id = uuid.uuid4()
        self.isim = isim
        self.parola = parola
        kullanicilar.append(isim,parola,id)
        return True

    def adres_defteri_ekle(self,adres_defteri):
        adresDefteri.append((adres_defteri))

    def adres_defteri_sil(self,adres_defteri):
        adresDefteri.remove(adres_defteri)


    # def kullanici_ekle(self,list):
    #     kullanicilar.append(list)
    #     print(kullanicilar)
    #
    #
    # def kullanici_sil(self,isim):
    #     if isim in kullanicilar:
    #         del kullanicilar[isim]
    #         print(kullanicilar)
    #         return True