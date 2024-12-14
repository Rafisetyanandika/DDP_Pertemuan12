class person:
    def __init__(self, nama, umur, jekel):
        self.nama = nama
        self.umur = umur
        self.jekel = jekel

    def jalan(self):
        print(f"{self.nama} bisa berjalan")  

    def ngomong (self):
        print(f"dia berbicara karena dia {self.jekel}")

class supir(person):
    def __init__(self, nama, umur, jekel, sim):
        super().__init__(nama, umur, jekel)
        self.sim = sim

    def nyupir (self):
        print(f"{self.nama} bisa nyupir karena memiliki sim{self.sim}")  

class mahasiswa(person):
    def __init__(self, nama, umur, jekel, nim):
        super().__init__(nama, umur, jekel)
        self.sim = nim 