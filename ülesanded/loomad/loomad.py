class Loomad():
    def __init__(self, jalad, korgus, toitumine, vanus):
        if jalad == True or jalad == False:
            self.jalad = jalad
        self.korgus = korgus
        if toitumine == "Taime" or toitumine == "Liha" or toitumine == "Sega":
            self.toitumine = toitumine
        self.vanus = vanus
    
    def kasva(self, kasv):
        self.korgus = kasv + self.korgus
        print(self.korgus)
        
    def vanane(self, vana):
        self.vanus = vana + self.vanus
        print(self.vanus)
        
class imetajad(Loomad):
    def __init__(self, jalad, korgus, toitumine, vanus, sugu):
        if sugu == "M" or sugu == "N":
            self.sugu = sugu
        self.vanus = vanus
        
    def sure(self):
        if self.vanus >= 211:
            self.surm = "Loom on dead"
        else:
            self.surm = "Loom on elus"
        print(self.surm)
        
    class inimene(imetajad):
        def __init__(self, jalad, korgus, toitumine, vanus, sugu, nimi, kodakondsus):
            self.nimi = nimi
            self.kodakondsus = kodakondsus
            
        def surm(self):
            if self.vanus > 121:
                self.surm = "Inimene on dead"
            else:
                self.surm = "Inimene on elus"
            print(self.surm)
            
        def valjastaandmed(self):
            print("Tere " + self.nimi + " , sa oled pärit " + self.kodakondsus + " . Sa oled " + self.vanus + " aastat vana ning oled " + self.korgus + " cm pikk" + ". Sa oled " + self.sugu + "soost ja sa oled " + self.toitumine + "toitlane.")



test = loomad(True, 89, "Taime", 21)