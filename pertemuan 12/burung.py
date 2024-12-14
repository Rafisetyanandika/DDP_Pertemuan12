from Animal import *
    
class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print("jenis \t\t\t\t: ", self.jenis, 
        "\nbunyi \t\t\t\t: ", self.bunyi)
gereja = burung("burung", "pur", "pohon", "bertelur", "gereja", "klutukklutuk") 
gereja.cetak_burung()      
print(" ")     

murai = burung("burung", "jangkrik", "kandang", "bertelur", "murai", "ngikkkkkngikkkkk") 
murai.cetak_burung()