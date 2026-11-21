#class and object

class Mahasiswa:
    nim = 0
    nama = ""
    
    def perkenalan (self):
        print(f"Perkenalkan nama saya {self.nama}")
        
    def hello (self, nama):
        print(f"Halo {self.nama}, Perkenalkan nama saya {nama}")
    
mahasiswa = Mahasiswa()
mahasiswa.nama = "Arya"
mahasiswa.perkenalan()
mahasiswa.hello("Budi")