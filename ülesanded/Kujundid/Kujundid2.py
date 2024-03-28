#Edgar Raudsepp IT-22 14.03.24
class Kujund:
    def __init__(self):
        self.nurkadeArv = 0
        self.pindala = 0

    def arvutaPindala(self):
        pass  

class Ring(Kujund):
    def __init__(self, raadius):
        super().__init__()
        self.raadius = raadius
        self.nurkadeArv = 0

    def arvutaPindala(self):
        self.pindala = 3.14 * self.raadius ** 2
        return self.pindala

class Ristkylik(Kujund):
    def __init__(self, korgus, laius):
        super().__init__()
        self.korgus = korgus
        self.laius = laius
        self.nurkadeArv = 4
    def arvutaPindala(self):
        self.pindala = self.korgus * self.laius
        return self.pindala

ring = Ring(3)
ring2 = Ring(5)
ristkylik = Ristkylik(4, 8)
ristkylik2 = Ristkylik(2, 4)

print(".")

print(f"Essa Ringi pindala: {ring.arvutaPindala()}")
print(f"Essa Ristküliku pindala: {ristkylik.arvutaPindala()}")

print(".")

print(f"Teise Ringi pindala: {ring2.arvutaPindala()}")
print(f"Teise Ristküliku pindala: {ristkylik2.arvutaPindala()}")