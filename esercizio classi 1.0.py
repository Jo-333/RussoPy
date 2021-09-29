class auto:

    garanzia = 1
    assicurazione = True
    parcoAuto = 0

    
    def __init__(self, proprietario, marca, tipo_carburante, modello, targa, colore, numero_sedili):

        self.proprietario = proprietario
        self.marca = marca
        self.tipo_carburante = tipo_carburante
        self.modello = modello
        self.targa = targa
        self.colore = colore
        self.numero_sedili = numero_sedili
        
        auto.parcoAuto +=1

    def setproprietario(self, value):
        self.proprietario = value

    def setmarca(self, value):
        self.marca = value

    def settipo_carburante(self, value):
        self.tipo_carburante = value

    def setmodello(self, value):
        self.modello = value

    def settarga(self, value):
        self.targa = value

    def setcolore(self, value):
        self.colore = value

    def setnumero_sedili(self, value):
        self.numero_sedili = value

    
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n Marca: {self.marca}\n tipo carburante: {self.tipo_carburante}\n Modello: {self.modello}\n Targa: {self.targa}\n colore: {self.colore}\n assicurazione: {self.assicurazione}\n numero_sedili: {self.numero_sedili} ' 
    
antonio = auto("antonio","BMW","Diesel", "Serie 2 Coupè","M HI 2614", "viola", "quattro" )

giovanna = auto("giovanna","Fiat","Benzina", "Panda 750","0807 ATX", "rossa", "quattro" )

print("Il tipo di variabile costruita è:")
print(antonio)
print(giovanna)

print("\nLa singola scheda è:")
print (antonio.scheda())
print (giovanna.scheda())
print("\nauto totali: ",auto.parcoAuto)

print("\n\naltro metodo per visualizzare le informazioni (__dict__):")

print(antonio.__dict__)
print(giovanna.__dict__)
