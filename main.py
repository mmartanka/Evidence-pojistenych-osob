from evidence import EvidencePojistenych
from pojisteny import Pojisteny
import time as _time

pojisteni = EvidencePojistenych() # vytvoření instance
pokracovat = True

print("\nEVIDENCE POJISTENYCH")
print("--------------------\n")

print("Vítejte v pojišťovně BECALM\n")
_time.sleep(1)

# vytvoření smyčky nabídky, dokud uživatel nezvolí konec programu

while pokracovat:
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
    print()
    
    if (volba == 1):
        # vytvoření pojištěného
        print("\nPŘIDÁNÍ NOVÉHO POJIŠTĚNÉHO\n")
        _time.sleep(1)
            
        # ošetření vstupu, aby jméno i příjmení bylo bez mezer na začátku i konci, aby začínalo velkým písmenem a neobsahovalo jiné znaky
        while True:
            jmeno = input("Zadejte křestní jméno pojištěného:\n").strip().capitalize()
            if not jmeno.isalpha():
                print("Chyba! Jméno smí obsahovat pouze písmena.\n")  # ošetření případných chyb při zadání
                _time.sleep(0.5)
            else:
                break
        while True:
            prijmeni = input("Zadejte příjmení pojištěného:\n").strip().capitalize()
            if not prijmeni.isalpha():
                print("Chyba! Příjmení smí obsahovat pouze písmena. \n")
                _time.sleep(0.5)
            else:
                break
        while True:
            vek = input("Zadejte věk pojištěného (pojištěný musí být plnoletý a nesmí být starší 80 let):\n").strip()
            if not vek.isdigit() or not 18 <= int(vek) <= 80:  # ošetření, aby byl věk celé číslo a v povoleném rozmězí
                print("Chyba! Věk pojištěného musí být celé číslo a v rozmezí 18 - 80.\n")
                _time.sleep(0.5)
            else:
                break # platný věk, ukončení cyklu
       
        while True:
            telefon = input("Zadejte telefonní číslo pojištěného:\n").strip()
            if not telefon.isnumeric() or len(telefon) != 9: #  kontrola, zda uživatel zadal 9 číslic a ne jiné znaky
                print("Chyba! Zadejte prosím telefonní číslo ve správném formátu, např. 723123123\n")
                _time.sleep(0.5)
            else:
                break
            
        novy_pojisteny = pojisteni.zalozit_pojisteneho(jmeno, prijmeni, vek, telefon)        
        input("\nNový pojištěný byl úspěšně uložen do evidence! Pokračujte stisknutím klávesy 'Enter'.\n")

    elif (volba == 2):
        # Výpis seznamu všech pojištěných pomocí metody zobraz_pojistene
        print("\nSEZNAM VŠECH POJIŠTĚNÝCH\n")
        _time.sleep(1)
        pojisteni.zobraz_pojistene()
        input("\nPokračujte stisknutím klávesy 'Enter'.\n")

            
    elif (volba == 3):
        if len(pojisteni.evidence) == 0:  # kontrola, zda databáze obsahuje nějaké položky
            print("Databáze pojištěných je prázdná.\n")
        else:
            while True:
                print("\nVYHLEDÁNÍ POJIŠTĚNÉHO\n") # vyhledá pojištěného z databáze podle jména, příjmení a ošetří správné zadání
                _time.sleep(1)
                jmeno = input("Zadejte křestní jméno pojištěného:\n").strip().capitalize()
                if not jmeno.isalpha():
                    print("Křestní jméno smí obsahovat pouze písmena.\n")
                else:
                    break
            while True:
                prijmeni = input("Zadejte příjmení pojištěného:\n").strip().capitalize()
                if not prijmeni.isalpha():
                    print("Příjmení smí obsahovat pouze písmena.\n")
                else: 
                    break
                
            pojisteni.najdi_pojisteneho(jmeno, prijmeni)  # v případě správného zadání se spustí vyhledávání

        input("\nPokračujte stisknutím klávesy 'Enter'.\n")
         
    elif (volba == 4):  # ukončení aplikace
        print("\nKONEC PROGRAMU\n")
        print("--------------------\n")
        _time.sleep(1)
        print("Děkujeme, že jste využili našich služeb!\n")
        pokracovat = False
    
    else:
        print("Neplatná volba! Zadejte číslo od 1 do 4.\n")
        input("\nPokračujte stisknutím klávesy 'Enter'.\n")
            
            
                    



        