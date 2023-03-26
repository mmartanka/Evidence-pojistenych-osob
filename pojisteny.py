class Pojisteny:
    """
    Třída reprezentuje jednotlivé pojištěné osoby.
    """

    # Construktor
    def __init__(self, jmeno, prijmeni, vek, telefon):
    
    # Vytvoření atributů
        """
        jmeno - jméno pojištěného
        prijmeni - příjmení pojištěného
        vek - věk pojištěného
        telefon - telefonní číslo pojištěného
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    """
    Vrací textovou reprezentaci pojištěných osob s mezerami.
    """

    def __str__(self):
        return (f"{self.jmeno}\t {self.prijmeni}\t {self.vek}\t {self.telefon}\n")
    


                                              
