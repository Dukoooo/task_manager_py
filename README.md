# Správca úloh (Task Manager) — jednoduchý Python skript

Jednoduchý konzolový správca úloh napísaný v Pythone. Tento projekt umožňuje pridávať, zobrazovať a odstraňovať úlohy cez textové menu. V zložke `task_part2` sú k dispozícii PDF test cases pre každú funkciu.

## Funkcie
- Pridať novú úlohu (názov + popis) s automatickým ID
- Zobraziť všetky úlohy v kontinuálnom číslovaní
- Odstrániť úlohu podľa poradia (indexu zoznamu)
- Ukončiť program

Funkcie v kóde:
- `pridat_ulohu()` — načíta názov a popis; overí, že vstupy nie sú prázdne; pridá úlohu do zoznamu `tasks`.
- `zobrazit_ulohy()` — vypíše všetky úlohy s poradovým číslom.
- `odstranit_ulohu()` — zobrazí úlohy, pýta sa na číslo úlohy na zmazanie a ak je platné, zmaže ju.
- `koniec_programu()` — ukončí program.
- `hlavne_menu()` — hlavné cyklické menu, ktoré prepája všetky vyššie uvedené funkcie.

## Požiadavky
- Python 3.6 alebo novší (pre f-strings a pohodlnú prácu so slovníkmi)

## Inštalácia a spustenie
1. Ulož súbor so skriptom (napr. `task_manager.py`) do projektu.
2. V termináli spusti:
```bash
python task_manager.py
```

(alebo `python3 task_manager.py` podľa konfigurácie tvojho systému)

## Použitie — príklad
Po spustení sa zobrazí menu:
```
Správca úloh - hlavné menu
1. Pridať novú úlohu
2. Zobraziť všetky úlohy
3. Odstraniť úlohu
4. Koniec programu
Vyberte možnosť (1-4):
```

Pridanie úlohy:
- Program sa spýta na názov a popis. Ak je ktorýkoľvek vstup prázdny, opýta sa znova.

Zobrazenie úloh:
- Zobrazia sa všetky úlohy v tvare `1. Názov - Popis`.

Odstránenie úlohy:
- Zadaj číslo (poradové) úlohy, ktorá sa má odstrániť. Ak zadáš neplatné číslo, program o tom informuje.

## Štruktúra projektu
- task_manager.py — hlavný skript so správcom úloh
- task_part2/ — zložka obsahujúca PDF test cases pre každú funkciu (pridať
