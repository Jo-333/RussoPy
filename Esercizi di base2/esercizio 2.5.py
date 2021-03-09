#Esercizio di base 2
#Crea un programma che scrive un file di testo che si chiama testo.txt e scrivi al suo interno 100 numeri casuali. Crea un altro programma che apre il file creato e restituisca a monitor i 100 numeri.
with open("testo.txt", "r") as f:
    for line in f: print(line, end="")
