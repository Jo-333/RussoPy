
from guizero import*

app = App(title= "Prodotto intermedio python" )

message = Text(app, text= "Questo programma permette di creare un grafico attraverso un file")

message = Text(app, text= " inserisci il nome del file:")

file = TextBox(app, text= "")

app.display()

print (file)

