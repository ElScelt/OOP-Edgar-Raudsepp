#Edgar Raudsepp IT-22 27.02.24
class Sõiduk:
    def __init__(self, nimi, maxKiirus, istekohtadeArv):
        self.nimi = nimi
        self.maxKiirus = maxKiirus
        self.istekohtadeArv = istekohtadeArv
        self.kiirus = 0  

    def valjastaAndmed(self):
        print(f"Nimi: {self.nimi}")
        print(f"Istekohtade arv: {self.istekohtadeArv}")
        print(f"Kiirus: {self.kiirus}")  

class Buss(Sõiduk):
    def __init__(self, nimi, maxKiirus, istekohtadeArv, piletiHind):
        super().__init__(nimi, maxKiirus, istekohtadeArv)
        self.piletiHind = piletiHind
        self.reisijaid = 0

    def ostaPilet(self, piletiteArv):
        if self.istekohtadeArv - self.reisijaid < piletiteArv:
            print(f"Ei ole piisavalt kohti. Vabu kohti: {self.istekohtadeArv - self.reisijaid}")
        else:
            self.reisijaid += piletiteArv
            print(f"Piletid ostetud! Reisijaid bussis: {self.reisijaid}")
            self.kiirus = 70  

    def valjastaAndmed(self):
        super().valjastaAndmed()
        print(f"Pileti hind: {self.piletiHind}")
        print(f"Reisijaid bussis: {self.reisijaid}")


buss = Buss("NR 14", 70, 50, 2.5)
buss.valjastaAndmed()
buss.ostaPilet(30)
buss.valjastaAndmed()
