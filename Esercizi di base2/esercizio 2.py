#Esercizi di base 2

#Chiedi all'utente una lista di 5 numeri interi e salvali in un Array.Ordina la lista e restituiscila in output nell'ordine inverso.
print("Inserisci 5 numeri interi: ")
Numeri = []
for x in range(5):
    numero = input()

    Numeri.append(numero)

print(list(reversed(Numeri)))




