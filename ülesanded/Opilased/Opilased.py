#Edgar Raudsepp IT-22 14.03.24
import random
class Inimene:
    nimi = 'teadmata'
    vanus = 0
    vanane = []

    def __init__(self,x,y):
        self.nimi = x
        self.vanus = y
        self.vanane = self.vanus + 1

    def kuva(self):
        print('Nimi: {} \nVanus: {} \nVananedes: {} '.format(self.nimi, self.vanus, self.vanane))


uusObjekt = Inimene("Kuusik", 21)
uusObjekt.kuva()


class Opilane(Inimene):
    def __init__(self):
        super().__init__()

    ryhm = 'teadmata'
    keskmineHinne = 0
    energia = 0
    puhka = 0
    opi = 0


    def __init__(self, x, y, c):
        self.puhka = x
        self.ryhm = "IT22"
        self.keskmineHinne = random.uniform(2,5)
        self.energia = c
        self.opi = self.keskmineHinne + 0.1

    def kuva1(self):
        print('Ryhm on: {} \nKeskmine Hinne on: {} \nEnergiat on: {} \nPuhka: {} \nOpi: {}  '.format(self.ryhm, self.keskmineHinne, self.energia, self.puhka, self.opi))

uusObjekt1 = Opilane(random.uniform(1,24), random.uniform(2,5), random.uniform(1,100) )
uusObjekt1.kuva1() # Ei tea kuidas puhka meetodit täpsemalt lisada ning kuidas ma välja prinditud numbrid saaks nii et need on ilma komakohtadeta ehk siis floatina?


class Opetaja(Inimene):
    def __init__(self, energia, opeta, puhka):
        super().__init__()
        self.energia = energia
        self.opeta = opeta
        if self.energia < 20: print('\nÕpetada ei saa kuna energiat on vähem kui 20'.format (self.opeta)) # ei saa hakkama sellega et kui see oleks vähem kui see energia kogus seal ülevalpool random energiaga on (ei oska seletada)
        puhka = puhka # ei tea kuidas ikkagi seda palli süsteemi teha mis annaks energiat juurde saan aru et puhkamis aeg + energiat olenedes tunnist








