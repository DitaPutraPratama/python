from contextlib import closing


class persegiPanjang:
    nama = 'gedung'
    panjang = 10
    lebar = 5

    def luas(self):
        self.luas = self.panjang*self.lebar

    def keliling(self):
        self.keliling = 2*(self.panjang+self.lebar)


class persegi:
    nama = 'blok'
    panjangSisi = 10

    def luas(self):
        self.luas = self.panjangSisi*self.panjangSisi

    def keliling(self):
        self.keliling = 4*self.panjangSisi
