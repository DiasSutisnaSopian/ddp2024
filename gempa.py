class Gempa:
    def __init__(self, skala, lokasi):
        self.skala = skala
        self.lokasi = lokasi

    def dampak(self):
        print(f"ada gempa baru nih di {self.lokasi}")
        print(f"skala dari gempa ini adalah {self.skala}")
        if self.skala < 2:
            print('dampak ga berasa')
        elif self.skala >= 2 and self.skala <= 4:
            print('bangunan retak - retak')
        elif self.skala > 4 and self.skala <= 6:
            print('bangunan roboh')
        elif self.skala > 6:
            print('bangunan roboh dan berpotensi tsunami')
        else :
            print('sistem tidak valid')

