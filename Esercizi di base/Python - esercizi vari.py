#ESERCIZI VARI


#Chiedi all'utente del programma il suo nome e restituiscilo come output.
nome = input('Inserisci il tuo nome: ')
print(nome)


#Chiedi all'utente il nome ed il cognome e restituiscili in output separati da uno spazio.
cognome = input('Inserisci il tuo cognome: ')


#stampa nome e cognome
print (nome, cognome)


#Chiedi all'utente il nome ed il cognome e restituisci in output il numero dei caratteri del nome e del cognome.
lunghezza_nome = len (nome)
print('il tuo nome è composto da ',lunghezza_nome, 'lettere')

lunghezza_cognome = len (cognome)
print('il tuo cognome è composto da ',lunghezza_cognome, 'lettere')


#Prendi In input due numeri e restituiscili ordinati, prima il più piccolo e poi più grande.
numero1 = input('inserisci il primo numero:')
numero2 = input('inserisci il secondo numero:')
a = [numero1, numero2]
a.sort()
print(a) 


#Chiedi all'utente il suo colore preferito, se digita: “rosso”, “Rosso” o “ROSSO” rispondi “bello” altrimenti rispondi “non mi piace”.
colore_preferito = input('Inserisci il tuo colore preferito:')
if colore_preferito == 'rosso':
    print ('bello')
elif colore_preferito == 'Rosso':
    print ('bello')
elif colore_preferito == 'ROSSO':
    print ('bello')

else: print ('non mi piace')


#Chiedi all'utente di scrivere il suo nome e restituisci in output tre volte il nome inserito dall'utente ( usa i cicli).
seq = [1, 2, 3]
for i in seq:
    print(nome )


#Chiedi all'utente il suo nome e restituisci in output tutte le lettere del nome, una alla volta.
s = nome
for x in s:
    print(x)


#Chiama una variabile “frutta” per salvare una tupla di 4 frutti diversi. Restituisci in output l'elemento associato al terzo indice.
frutta = 'banana, pesca, anguria e kiwi'
print (frutta[15:22])


#Costruisci una tupla con quattro elementi e chiedi all'utente di sceglierne uno, restituisci in output l’indice dell’elemento scelto dall’utente.(nome.index(”nome”))

elements = 'martello, penna, matita, scala'
print('Scegli un elemento e scrivilo')
print(elements)
elemento_scelto = input('Inserisci elemento: ')
print (elemento_scelto)



#Costruisci una lista di 5 elementi e restituisci in output tutti gli elementi attraverso un ciclo.
seq2 = [1]
elements2 = 'calcolatrice, telefono, scrivania, tastiera, cornice'
for i in seq2:
    print (elements2)


#Costruisci una lista di 10 elementi ed ordinala in automatico attraverso il metodo Sort.
lista = ['patata','carota', 'maiale', 'casa', 'villaggio', 'aereo', 'elicottero', 'libro', 'dizionario', 'finestra']
lista.sort()
print(lista)


#Si scriva un file JSON che includa 10 libri di una libreria, ogni libro avrà dei campi, ad esempio: titolo, autore, genere ecc
import json
data = {'libri': [{'I Promessi Sposi': 'Manzoni', 'Romanzo storico': '11,40$'},
                  {'Divina Commedia': 'Dante Alighieri', 'Poema': '29,00$'},
                  {'Iliade': 'Omero', 'Poema': '22,80$'},
                  {'Eneide': 'Virgilio', 'Poema': '2,99$'},
                  {'Nome della Rosa': 'Umberto Eco', 'Romanzo': '17,10$'},
                  {'La solitudine dei numeri primi': 'Paolo Giordano', 'Romanzo': '8$'},
                  {'Resto Qui': 'Marco Balzano', 'Romanzo': '9,20$'},
                  {'Io,robot': 'Isaac Asimov', 'Fantascienza': '13.30$'},
                  {'Fondazione': 'Isaac Asimov', 'Fantascienza': '30,40$'},
                  {'The outsider': 'Stephen King', 'Narrativo': '9,99$'}]}
with open("output.json", "w") as outfile:
    json.dump(data, outfile)

print(data)























    











