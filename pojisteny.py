class Pojisteny:

    # konstruktor třídy
    def __init__(self, jmeno, prijmeni, vek, telefon):
    
    # vytvoření atributů
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):  # vrací textovou reprezentaci pojištěných osob
        return (f"{self.jmeno}\t {self.prijmeni}\t {self.vek}\t {self.telefon}\n")
    


                                              
