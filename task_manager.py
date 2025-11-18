def pridat_ulohu():
    print("Funkcia pridat_ulohu() bola spustena.")

def zobrazit_ulohy():
    print("Funkcia zobrazit_ulohy() bola spustena.")

def odstranit_ulohu():
    print("Funkcia odstranit_ulohu() bola spustena.")

def hlavne_menu():
    while True:
        print("\nSpravca uloh - hlavne menu")
        print("1. Pridat novu ulohu")
        print("2. Zobrazit vsetky ulohy")
        print("3. Odstranit ulohu")
        print("4. Koniec programu")

        volba = input("Vyberte moznost (1-4): ")

        if volba == '1':
            pridat_ulohu()
        elif volba == '2':
            zobrazit_ulohy()
        elif volba == '3':
            odstranit_ulohu()
        elif volba == '4':
            print("Program konci, ahoj!")
            break
        else:
            print("Neplatna volba, skuste to znovu.")

hlavne_menu()
