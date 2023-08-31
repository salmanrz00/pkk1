class kendaraan:
    def __init__(self, name):
        self.name = name
        self.penumpang = []
    def tambah_penumpang(self, name_penumpang):
        self.penumpang.append(nama_penumpang)

class mobil(kendaraan):
    pintu_terbuka = False
    def buka_pintu(self):
        self.pintu_terbuka = True
    def tutup_pintu(self):
        self.pintu_terbuka = False
    def welcome(self):
        print("selamat datang! silahkan duduk")

mobil = mobil("mobil tesla")
print(f"nama kendaraan:{mobil.nama}")
mobil.tambah_penumpang("ilham")
mobil.tambah_penumpang("abel")
print(f"penumpang: {mobil.tambah_penumpang}")
mobil.buka_pintu()
print(f"pintu terbuka: {mobil.pintu_terbuka}")
mobil.tutup_pintu()
print(f"pintu tertutup: {mobil.pintu_tertutup}")
mobil.welcome()
