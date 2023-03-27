from pojisteny import Pojisteny

class EvidencePojistenych:

    def __init__(self):
        self.evidence = []

    def zalozit_pojisteneho(self, jmeno, prijmeni, vek, telefon):  # metoda pro vytvoření nového pojištěného 
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.evidence.append(pojisteny)
                   
    def zobraz_pojistene(self):  # metoda pro výpis pojištěných z databáze
        for pojisteny in self.evidence:
            print(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):  # metoda pro vyhledání pojištěného podle jména a příjmení
        for pojisteny in self.evidence:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print(f"\n{pojisteny}")
          
                    