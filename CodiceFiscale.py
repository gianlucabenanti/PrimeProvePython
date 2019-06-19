#chiedo di inserire i dati
Nome = input("Inserisci il nome: ").upper()
#Cognome = input("Inserisci il cognome: ").upper()
#Sesso = input("Inserisci il tuo sesso (M per maschio ed F per femmina): ").upper()
#Luogo = input("Inserisci il tuo luogo di nascita: ")
#Data = input("Inserisci la tua data di nascita (gg/mm/aaaa): ")

#inizializzo l'array delle consonanti
Consonanti = ["B","C","D","F","G","H","L","M","N","P","Q","R","S","T","V","Z"]

#verifico che la data sia corretta
#if not (Data[:2].isalnum() and Data[3:5].isalnum() and Data[6:10].isalnum()):
#    print("data non corretta")

b = ""

for i in range(0,Nome.__len__()):
    a = Nome[i]
    for j in range(0,Consonanti.__len__()):
        if a == Consonanti[j]:
            b += a


