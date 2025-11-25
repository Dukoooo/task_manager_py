tasks = []


# # funkcia ktorá kontroluje či vstup obsahuje aspon 3 písmená
# def contains_three_letters(text):
#     return sum(c.isalpha() for c in text) >= 3



# funkcia zabezbečí že vložené údaje budú správne, a ak nie, voľba sa opakuje
def pridat_ulohu():
    
    while True:
        task_name = input("Zadajte názov úlohy:" ).strip()
        task_des = input("Zadajte popis úlohy: " ).strip()
      
        if task_name != "" and task_des != "":
            task_ID  = int(len(tasks) + 1)
            tasks.append({"name": task_name, "description": task_des, "ID":task_ID})
            print(f"Úloha č. {task_ID} bola úspešne pridaná.\n")
            hlavne_menu()
            break
        else:
            print("Zadali ste prázdny vstup, opakujte voľbu prosím.")
            continue
            


# funkcia na zobrazenie úloh s kontinuálnym číslovaním
def zobrazit_ulohy():
    if tasks:
        print("Zoznam úloh: ")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['name']} - {task['description']}")
    else:
        print("Žiadne tasky k dispozícii...")

# funkcia na odstránenie úlohy podľa poradia
def odstranit_ulohu():
    zobrazit_ulohy()
    if not tasks:
        return
    option = int(input("Zadajte číslo úlohy ktorú chcete zmazať: "))
    if 1 <= option <= len(tasks):
        removed_task = tasks.pop(option-1)
        print(f"Úloha '{removed_task['name']}' bola zmazaná.")
    else:
        print("Zadané číslo nie je platné.")
      


def koniec_programu():
    print("Koniec programu.\n")
    exit()

def hlavne_menu():
    while True:
        print("\nSprávca úloh - hlavné menu")
        print("1. Pridať novú úlohu")
        print("2. Zobraziť všetky úlohy")
        print("3. Odstraniť úlohu")
        print("4. Koniec programu")
        option = input("Vyberte možnosť (1-4): ")
        print("\n")

        if option == '1':
            pridat_ulohu()
        elif option == '2':
            zobrazit_ulohy()
        elif option == '3':
            odstranit_ulohu()
        elif option == '4':
            koniec_programu()
            
            break
        else:
            print("Neplatná voľba, skúste to znovu prosím.")

hlavne_menu()
