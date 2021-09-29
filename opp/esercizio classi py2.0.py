class Studente:

    def __init__(self, nome, cognome, corso_di_studi, età, sesso, ID):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
        self.età = età
        self.sesso = sesso
        self.ID = ID

    def setnome(self, value):
        self.nome = value

    def setcognome(self, value):
        self.cognome = value

    def setcorso_di_studi(self, value):
        self.nome = value

    def setetà(self, value):
        self.età = value

    def setsesso(self, value):
        self.sesso = value

    def setID(self, value):
        self.ID = value

    def scheda_personale(self):
        return f"Scheda Studente{self.ID}:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso di Studi:{self.corso_di_studi}\n Età:{self.età}\n Sesso:{self.sesso}"
studente_uno = Studente("Marco","Rossi", "Ingegneria", "21 anni", "Uomo", 1)
studente_due = Studente("Anna","Austro", "Moda", "23 anni", "Donna", 2)
studente_tre = Studente("Andreea","Valentini", "Matematica", "19 anni", "Donna", 3)
studente_quattro = Studente("Antonio","Esposito", "Programmazione", "22 anni", "Uomo", 4)


print(studente_uno.scheda_personale())
print(studente_due.scheda_personale())
print(studente_tre.scheda_personale())
print(studente_quattro.scheda_personale())


