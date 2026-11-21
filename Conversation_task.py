#Membuat class
class Karyawan:
    def __init__(self, nama, asal, id_kerja, departemen):
        self.nama = nama
        self.asal = asal
        self.id_kerja = id_kerja
        self.departemen = departemen

    def perkenalan(self):
        print(f"{self.nama}: Halo, nama saya {self.nama}.")

    def tanya_asal(self, orang):
        print(f"{self.nama}: Dari mana asal kamu, {orang.nama}?")

    def jawab_asal(self):
        print(f"{self.nama}: Saya berasal dari {self.asal}.")

    def tanya_id(self, orang):
        print(f"{self.nama}: Berapa ID kerja kamu, {orang.nama}?")

    def jawab_id(self):
        print(f"{self.nama}: ID kerja saya adalah {self.id_kerja}.")

    def menyadari_departemen(self, orang):
        if self.departemen == orang.departemen:
            print(f"{self.nama}: Oh, ternyata kamu satu departemen dengan saya!")
            print(f"{self.nama}: Kita sama-sama dari departemen {self.departemen}.")
        else:
            print(f"{self.nama}: Oh, ternyata kita berbeda departemen.")
    def menuju_meja(self):
        print(f"{self.nama}: Mari kita menuju tempat duduk bersama.")

    def duduk(self):
        print(f"{self.nama}: Baik, mari kita duduk bersama.")

    def selesai(self):
        print(f"{self.nama}: Senang berkenalan denganmu!")


# Membuat object
karyawan1 = Karyawan("Ciko", "Jakarta", "KNG001", "Keuangan")
karyawan2 = Karyawan("Dito", "Bandung", "KNG002", "Keuangan")


print("===== PERCAKAPAN DI KANTOR =====\n")


karyawan1.perkenalan()
karyawan2.perkenalan()


print()
karyawan1.tanya_asal(karyawan2)
karyawan2.jawab_asal()

karyawan2.tanya_asal(karyawan1)
karyawan1.jawab_asal()


print()
karyawan1.tanya_id(karyawan2)
karyawan2.jawab_id()


karyawan1.menyadari_departemen(karyawan2)


print()
karyawan2.tanya_id(karyawan1)
karyawan1.jawab_id()


print()
karyawan1.menuju_meja()
karyawan2.duduk()


print()
karyawan1.selesai()
karyawan2.selesai()

print("\n===== PERCAKAPAN SELESAI =====")
