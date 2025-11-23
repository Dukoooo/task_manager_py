import re
tasks = []

# vytvorenie regex funkcie na validáciu či input naozaj obsahuje iba písmená (povolenie písmen všetkých jazykov)
def is_valid(text):
    return bool(re.fullmatch(r"[^\W\d_ ]+( [^\W\d_ ]+)*", text))



# funkcia zabezbečí že vložené údaje budú správne, a ak nie, voľba sa opakuje
def pridat_ulohu():
    
    while True:
        task_name = input("Zadajte názov úlohy:" ).strip()
        task_des = input("Zadajte popis úlohy: " ).strip()
      
        if is_valid(task_name) and is_valid(task_des):
            task_ID  = int(len(tasks) + 1)
            tasks.append({"name": task_name, "description": task_des, "ID":task_ID})
            print(f"Úloha č. {task_ID} bola úspešne pridaná.\n")
            hlavne_menu()
            break
        else:
            print("Zadali ste neplatné údaje...")
            continue
            

# funkcia na zobrazenie úloh
def zobrazit_ulohy():

    if tasks != []:
        print("Zoznam úloh: ")
        for task in tasks:
            print(f"{task["ID"]}. {task['name']} - {task['description']}")
    else:
        print("Žiadne tasky k dispozícii...")


def odstranit_ulohu():
    zobrazit_ulohy()
    option = int(input("Zadajte cislo ulohy ktoru chcete zmazat: "))

    for task in tasks:
        if task["ID"] == option:
            tasks.remove(task)
            print(f"Úloho číslo {task["ID"]} bola zmazaná.")
            hlavne_menu()
            break
        else:
            print(f"Žiadna úloha nenájdená pod číslom {str(option)}")
            odstranit_ulohu()
            


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
            print("Neplatná voľba, skúste to znovu prosím.")

hlavne_menu()
