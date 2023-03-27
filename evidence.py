from pojisteny import Pojisteny

class EvidencePojistenych:

    def __init__(self):
        # list pro uložení pojištěnců
        self.evidence = []

    def zalozit_pojisteneho(self, jmeno, prijmeni, vek, telefon):  # metoda pro vytvoření nového pojištěného 
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.evidence.append(pojisteny)
                   
    def zobraz_pojistene(self):  # metoda pro výpis pojištěných z databáze
        for pojisteny in self.evidence:
            print(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):  # metoda pro vyhledání pojištěného podle jména a příjmení
        nalezeno = False
        for pojisteny in self.evidence:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print(f"\n{pojisteny}")
                nalezeno = True  
            # v případě, že v databázi nebude nalezeno
            if nalezeno:
                pass
            else:
                print("\nZadané údaje se neshodují s žádným záznamem v databázi.")
          
                    