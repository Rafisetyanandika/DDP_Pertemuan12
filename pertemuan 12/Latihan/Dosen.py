from Person import *
class Dosen(Person):
    gelar = ""
    jabatan = ""
    gaji = 0

    def _init_(self, nama, gender, umur, gelar, jabatan):
        super()._init_(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan 
    
    def setGaji(self,uang):
        self.gaji = uang
    
    def cetak(self):
        super().cetak()
        print("Gelar \t\t :", self.gelar,
              "\nJabatan \t :", self.jabatan,
              "\nGaji \t\t : Rp.", self.gaji,
              "\n-------------------------------")