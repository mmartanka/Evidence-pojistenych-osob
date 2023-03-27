from pojisteny import Pojisteny

class EvidencePojistenych:

    def __init__(self, evidence):
        self.evidence = evidence 

    def __iter__(self):
        return iter(self.evidence)

    def zalozit_pojisteneho (self, jmeno, prijmeni, vek, telefon):
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.evidence.append(pojisteny)
        return pojisteny
                   
    def zobraz_pojistene(self):
        for pojisteny in self.evidence:
            print(pojisteny)

    def najdi_pojisteneho (self, jmeno, prijmeni):
        for pojisteny in self.evidence:
            if pojisteny.jmeno.lower() == jmeno and pojisteny.prijmeni.lower() == prijmeni:
                return pojisteny
        return None
                    