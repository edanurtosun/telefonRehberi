import uuid

from adresdefteri import AdresDefteri
kayit_gonder = AdresDefteri

# from kullanici import Kullanici
#
# kayitlar = list()
#
# kullanici_kaydet = Kullanici()
# silinecek_kullanici = Kullanici()

class Kayit:

    def __init__(self,defter_isim,isim,soyisim,telefon):
        self.id = uuid.uuid4()
        self.defter_isim = self.defter_isim
        self.isim = isim
        self.soyisim = soyisim
        self.telefon = telefon

        kayit = {
            'id' : self.id,
            'isim' : isim,
            'soyisim' : soyisim,
            'tel' : telefon
        }
        a = kayit_gonder.deftere_kayit_ekle(defter_isim,kayit)
        if a == True:
            return True
        else:
            return False



    # def kayit_ekle(self,isim,parola,telefon_numarasi,e_posta):
    #         kisi = {
    #             'isim': isim,
    #             'parola': parola,
    #             'tel' : telefon_numarasi,
    #             'e-posta':e_posta
    #         }
    #         kayitlar.append(kisi)
    #         kullanici_kaydet.kullanici_ekle(kisi)
    #         print("kayitlar")
    #         print(kayitlar)
    #         print("******************************")
    #         print(type(kayitlar))
    #         print("******************************")
    #         print(type(kayitlar[0]))
    #         print("******************************")
    #         print(kayitlar[0]['isim'])
    #         return True
    #
    # def kayit_sil(self,isim):
    #     silinecek_kullanici.kullanici_sil(isim)
    #
    # def kayit_kontrol(self,isim,parola):
    #     while i:
    #         i=0
    #         if kayitlar[i]['isim'] == isim and kayitlar[i]['parola'] == parola:
    #             return True
    #         else:
    #             return False
    #         i += 1
