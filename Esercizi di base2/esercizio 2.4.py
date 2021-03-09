#Esercizio di base 2
#Crea un programma che scrive un file di testo che si chiama testo.txt e scrivi al suo interno 100 numeri casuali. Crea un altro programma che apre il file creato e restituisca a monitor i 100 numeri.
from random import randint

Numeri = 100

with open("testo.txt", "w") as f:
    for i in range(Numeri):
        f.write(str(randint(1,100)) + "\n")

