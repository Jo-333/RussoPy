#Esercizi di base 2
#Crea una lista bidimensionale di numeri casuali, tre righe per tre colonne e chiedi all'utente quale riga vuole visualizzare.
from random import randint
Riga = 3
Colonne = 3

Griglia = []
for c in range(Riga):
    Colonna = [randint(1,100), randint(1,100), randint(1,100)]
    Griglia.append(Colonna)

print(Griglia)
for c in range(len(Griglia)):
    print(Griglia[c])
selezione_Riga = int(input("Scegli una riga: ")) - 1
selezione_Colonna = int(input("Scegli una colonna: ")) - 1

print(f"L'elemento selezionato è {Griglia[selezione_Riga][selezione_Colonna]}")
