# helloworld.py

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.spp_terbayar = False
        self.mata_kuliah = []
        self.nilai_akhir = {}

    def bayar_spp(self):
        print(f"{self.nama} sedang membayar SPP...")
        self.spp_terbayar = True
        print("SPP berhasil dibayar!")

    def daftar_mata_kuliah(self, mata_kuliah):
        if self.spp_terbayar:
            self.mata_kuliah.append(mata_kuliah)
            print(f"{self.nama} berhasil mendaftar mata kuliah {mata_kuliah}.")
        else:
            print("SPP belum dibayar. Tidak bisa mendaftar mata kuliah.")

    def ikuti_perkuliahan(self):
        if not self.mata_kuliah:
            print("Belum ada mata kuliah yang diambil.")
            return
        for mk in self.mata_kuliah:
            print(f"{self.nama} mengikuti perkuliahan {mk}.")

    def ujian(self, mata_kuliah, nilai):
        if mata_kuliah in self.mata_kuliah:
            print(f"{self.nama} mengikuti ujian {mata_kuliah} dengan nilai {nilai}.")
            self.nilai_akhir[mata_kuliah] = nilai
        else:
            print(f"{mata_kuliah} belum terdaftar dalam mata kuliah yang diambil.")

    def tampilkan_nilai_akhir(self):
        print(f"Nilai akhir {self.nama}:")
        for mk, nilai in self.nilai_akhir.items():
            print(f"{mk}: {nilai}")


# Proses simulasi
if __name__ == "__main__":
    # Buat objek Mahasiswa
    mahasiswa1 = Mahasiswa("Budi", "123456")

    # Langkah-langkah
    mahasiswa1.bayar_spp()                        # Bayar SPP
    mahasiswa1.daftar_mata_kuliah("Algoritma")    # Daftar mata kuliah
    mahasiswa1.daftar_mata_kuliah("Struktur Data")
    
    mahasiswa1.ikuti_perkuliahan()                # Mengikuti kuliah
    mahasiswa1.ujian("Algoritma", 85)             # Mengikuti ujian dan input nilai
    mahasiswa1.ujian("Struktur Data", 90)
    
    mahasiswa1.tampilkan_nilai_akhir()            # Tampilkan nilai akhir
