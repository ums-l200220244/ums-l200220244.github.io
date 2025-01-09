from metaflow import FlowSpec, step

class KuliahFlow(FlowSpec):

    @step
    def start(self):
        """Mulai Proses: Bayar SPP"""
        print("Bayar SPP...")
        self.spp_terbayar = True
        print("SPP telah dibayar!")
        self.next(self.daftar_mata_kuliah)

    @step
    def daftar_mata_kuliah(self):
        """Mendaftar Mata Kuliah"""
        if self.spp_terbayar:
            self.mata_kuliah = ["Algoritma", "Struktur Data"]
            print("Mendaftar mata kuliah:", ", ".join(self.mata_kuliah))
        else:
            print("SPP belum dibayar, tidak bisa mendaftar mata kuliah.")
        self.next(self.ikut_kuliah)

    @step
    def ikut_kuliah(self):
        """Mengikuti Kuliah"""
        for mk in self.mata_kuliah:
            print(f"Mengikuti perkuliahan: {mk}")
        self.next(self.ujian)

    @step
    def ujian(self):
        """Mengikuti Ujian dan Mendapatkan Nilai"""
        self.nilai = {"Algoritma": 85, "Struktur Data": 90}
        for mk, nilai in self.nilai.items():
            print(f"Ujian {mk} selesai. Nilai: {nilai}")
        self.next(self.end)

    @step
    def end(self):
        """Akhir Proses: Menampilkan Nilai Akhir"""
        print("Nilai akhir:")
        for mk, nilai in self.nilai.items():
            print(f"{mk}: {nilai}")
        print("Proses kuliah selesai!")

if __name__ == '__main__':
    KuliahFlow()
