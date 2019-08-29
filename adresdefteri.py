import uuid

# adresDefteri = list()
defter = []

kisiler = []

class AdresDefteri:

    def __init__(self,isim):
        self.id = uuid.uuid4()
        self.isim = isim
        adresdefteri = {
            'id' : self.id,
            'kategori' : isim
        }
        defter.append(adresdefteri)
        print(defter)
        print("*********")
        print(self.id)
        return True

    def deftere_kayit_ekle(self, defter_ad,kisi):
        defter_ad = []
        defter_ad.append(self.kisi)
        print(defter_ad)
        return True

    def defterden_kayit_sil(self,kisi):
        kisiler.remove(self.kisi)





    # def adres_defteri_olustur(self):
    #     defter = {
    #         'kategori': None,
    #         'isim': None,
    #         'tel': None,
    #         'e-posta': None
    #     }
    #     adresDefteri.append(defter)
    #     print(adresDefteri)
    #     return True
    #
    #
    #
    # def deftere_kayit_ekle(self,kategori,isim,tel,e_posta):
    #     defter= {
    #         'kategori':kategori,
    #         'isim' : isim,
    #         'tel' : tel,
    #         'e-posta':e_posta
    #     }
    #     adresDefteri.append(defter)
    #     print(adresDefteri)
    #     return True
    #
    # def adres_defteri(self):
    #     print(adresDefteri)
    #
    # def adres_defteri_sil(self,kategori):
    #     return True





