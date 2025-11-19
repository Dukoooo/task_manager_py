tasks = []

def pridat_ulohu():
    
    while True:
        task_name = input("Zadajte názov úlohy: " )
        task_des = input("Zadajte popis úlohy: " )

        if task_name != "" and task_des != "":
            tasks.append({"name": task_name, "description": task_des})
        else:
            print("Zadali ste neplatné údaje...")
        break

def zobrazit_ulohy():
    count = 0
    if tasks != []:
        for task in tasks:
            count += 1
            print("Zoznam úloh: ")
            print(f"{count} {task['name']} - {task['description']}")
    else:
        print("Žiadne tasky k dispozícii...")


def odstranit_ulohu():
    print("Funkcia odstranit_ulohu() bola spustena.")


def koniec_programu():
    hlavne_menu.destroy()

def hlavne_menu():
    while True:
        print("\nSpravca uloh - hlavne menu")
        print("1. Pridat novu ulohu")
        print("2. Zobrazit vsetky ulohy")
        print("3. Odstranit ulohu")
        print("4. Koniec programu")
        option = input("Vyberte moznost (1-4): ")
        print("\n")

        if option == '1':
            pridat_ulohu()
        elif option == '2':
            zobrazit_ulohy()
        elif option == '3':
            odstranit_ulohu()
        elif option == '4':
            print("Program konci, ahoj!")
            break
        else:
            print("Neplatna volba, skuste to znovu.")

hlavne_menu()
