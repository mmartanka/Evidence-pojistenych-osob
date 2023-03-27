from evidence import EvidencePojistenych
from pojisteny import Pojisteny

print("\nEVIDENCE POJISTENYCH")
print("--------------------\n")

# Vytvoření databáze evidence pojištěných
pojistenci = EvidencePojistenych([])


# Vytvoření nabídky
import time as _time
print("Vítejte v pojišťovně BECALM\n")
_time.sleep(1)

# Vytvoření smyčky nabídky, dokud uživatel nezvolí konec programu
while True:
    print("Zvolte akci, kterou chcete provést: \n")
    _time.sleep(1)
    print("1 - Přidat nového pojištěného")
    _time.sleep(0.5)
    print("2 - Vypsat seznam všech pojištěných")
    _time.sleep(0.5)
    print("3 - Vyhledat pojištěného")
    _time.sleep(0.5)
    print("4 - Konec programu")
    _time.sleep(1)

    volba = int(input("\nVaše volba:\n"))
    
    if (volba == 1):
        # Vytvoření pojištěného
        print("\nPŘIDÁNÍ NOVÉHO POJIŠTĚNÉHO\n")
        _time.sleep(1)
        
        # Ošetření vstupu, aby jméno i příjmení bylo bez mezer na začátku i konci, aby začínalo velkým písmenem a neobsahovalo jiné znaky
        jmeno = ""
        prijmeni = ""
        while not jmeno.isalpha() or not prijmeni.isalpha():
            jmeno = input("Zadejte jméno pojištěného:\n").strip().capitalize()
            prijmeni = input("Zadejte příjmení pojištěného:\n").strip().capitalize()
            if not jmeno.isalpha() or not prijmeni.isalpha():
                print("Chyba! Jméno a příjmení smí obsahovat pouze písmena. \n")
                _time.sleep(0.5)
           
        vek = ""
        while True:
            try:
                vek = int(input("Zadejte věk pojištěného (pojištěný musí být plnoletý a nesmí být starší 80 let):\n").strip())
                if 18 <= vek <= 80:
                    break # platný věk, ukončení cyklu
                else:
                    print("Chyba! Zadejte číslo v rozmezí 18 - 80.\n")
                    _time.sleep(0.5)
            except ValueError:
                print("Chyba! Zadejte platné číslo.\n")
                _time.sleep(0.5)

        telefon = ""
        while True:
            try:
                telefon = int(input("Zadejte telefonní číslo pojištěného ve formátu +420xxxxxxxxx:\n+420").strip())
                if len(str(telefon)) == 9 and str(telefon).isdigit(): #  Kontrola, zda uživatel zadal 9 číslic a ne jiné znaky
                    break  # platné telefonní číslo, ukončení cyklu
            except ValueError:
                print("Chyba! Zadejte prosím telefonní číslo ve správném formátu.\n")
                _time.sleep(0.5) 
            
        novy_pojisteny = pojistenci.zalozit_pojisteneho(jmeno, prijmeni, vek, telefon)
        print("\nPojištěný/á", novy_pojisteny.jmeno, novy_pojisteny.prijmeni,  "byl úspěšně přidán do evidence. Pokračujte libovolnou klávesou.\n")

    elif (volba == 2):
        # Výpis seznamu všech pojištěných pomocí metody zobraz_pojistene
        print("\nSEZNAM VŠECH POJIŠTĚNÝCH\n")
        _time.sleep(1)

        Pojisteny.zobraz_pojistene()
        

    elif (volba == 3):
        # Vyhledá pojištěného buď podle jména a příjmení, nebo podle věku - záleží na volbě uživatele
        print("\nVYHLEDÁNÍ POJIŠTĚNÉHO\n")
        _time.sleep(1)
        print("Podle čeho chcete vyhledat pojištěného?\n")
        _time.sleep(0.2)
        print("1 - vyhledat podle jména a příjmení:")
        print("2 - vyhledat podle telefonního čísla:\n")
        
        # Ošetření vstupu, aby volba byla 1 nebo 2
        while True:
            try:
                vyber = int(input("Zadejte volbu:\n"))
                if vyber == 1 or vyber == 2:
                    break  # platná volba, ukončení cyklu
                else:
                    print("Neplatná volba. Zadejte 1 nebo 2.\n")
            except ValueError:
                print("Neplatný vstup. Zadejte znovu.\n")
            

        if (vyber == 1):
            hledane_jmeno = input("Zadejte jméno a příjmení pojištěného:\n").strip().capitalize()
            for pojisteny in pojistenci:
                if hledane_jmeno == jmeno or hledane_jmeno == prijmeni:
                    print(pojisteny)
                    _time.sleep(0.3)

        elif (vyber == 2):
            hledane_cislo = input("Zadejte telefonní číslo pojištěného ve formátu +420xxxxxxxxx:\n").strip()
            for pojisteny in pojistenci:
                if hledane_cislo == telefon:
                    print(pojisteny)
        break

    else: 
        (volba == 4)
        print("\nKONEC PROGRAMU\n")
        print("--------------------\n")
        _time.sleep(1)
        print("Děkujeme, že jste využili našich služeb!\n")
        exit()
            
                    



        