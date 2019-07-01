# inizializzo il dizionario
Anagrafica = {}

# chiedo di inserire i dati
Anagrafica["Nome"] = input( "Inserisci il nome: " ).upper()
Anagrafica["Cognome"] = input( "Inserisci il cognome: " ).upper()
#Anagrafica["Sesso"] = input("Inserisci il tuo sesso (M per maschio ed F per femmina): ").upper()
#Anagrafica["Luogo"] = input("Inserisci il tuo luogo di nascita: ")
#Anagrafica["Data"] = input("Inserisci la tua data di nascita (gg/mm/aaaa): ")

# verifico che la data sia corretta
# if not (Data[:2].isalnum() and Data[3:5].isalnum() and Data[6:10].isalnum()):
#    print("data non corretta")

def consonanti(stringa):
    b = ""
    # inizializzo l'array delle consonanti
    Consonanti = ["B", "C", "D", "F", "G", "H", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "Z"]

    for a in stringa:
            if a in Consonanti:
                b = b + a
    return b

def consonanti2(stringa):
    Consonanti = ["B", "C", "D", "F", "G", "H", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "Z"]
    mylist = [i for i in stringa if i in Consonanti]
    return mylist


b = consonanti2(Anagrafica["Nome"])
CF_Nome = b[0] + b[2] + b[3]

b = consonanti(Anagrafica["Cognome"])
CF_Cognome = b[0] + b[1] + b[2]

print( CF_Cognome+CF_Nome )