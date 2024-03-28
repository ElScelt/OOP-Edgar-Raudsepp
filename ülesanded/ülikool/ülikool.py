class Tudeng:
    def __init__(self, nimi, tudengikood, aste, teaduskond):
        self.nimi = nimi
        self.aste = aste
        self.teadusNimi = teaduskond
        self.tudengikood = tudengikood

    def prindi(self):
        print(f"{self.nimi} | {self.tudengikood} |{self.aste} | {self.teaduskond} | {self.loputooteema}")

class BakalaureuseTudeng(Tudeng):
    def __init__(self, nimi, tudengikood, teaduskond, loputooteema):
        super().__init__(nimi, tudengikood, "Bakalaureus", teaduskond)
        self.loputooteema = loputooteema

    def tervita(self):
        print(f"{self.nimi} | {self.tudengikood} | {self.oppeaste} | {self.teaduskond} | {self.loputooteema}")

class MagistriTudeng(Tudeng):
    def __init__(self, nimi, tundengikood, teaduskond, juhendaja):
        self.juhendaja = juhendaja            

class Teaduskond:
    def __init__(self, nimi, juhataja):
    self.nimi = nimi
    self.juhataja = juhataja

tehnika = Teaduskond("Tehnika", "Madis")
insener = Teaduskond("Inseneriteaduskond", "Peeter")
majandus = Teaduskond("Majandusteaduskond", "Kadri")


tudeng1 = BakalaureuseTudeng("Rob", "5000", "BAKA", "IT", "x Teema")
tudeng2 = Magister("Karl","54321","Insener","Peeter")
tudeng1.tervita()
tudeng2.tervita()