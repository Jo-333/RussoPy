#Esercizi di base 2
#Costruisci un Array con 5 numeri casuali compresi fra 1 e 8. Fai scegliere all'utente uno dei numeri dell'array e restituisci in output il numero di volte che si ripete il numero scelto.
from random import randint
Numeri = []

for x in range(5):
    numero=randint(1,8)
    Numeri.append(numero)

print(Numeri)

Numero = input("Scegli un numero tra gli ultimi, e io lo conterò:")
counter = 0
for c in Numeri:
    if (Numero == str(c)):
        counter += 1

print(f"Il numero {Numero} risulta {counter} volte") 
