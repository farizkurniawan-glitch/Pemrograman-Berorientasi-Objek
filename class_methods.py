class mahasiswa :
    nim = 0
    nama = ""
    
    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")
        
mahasiswa = mahasiswa ()
mahasiswa.nama = "Arya"
mahasiswa.perkenalan()