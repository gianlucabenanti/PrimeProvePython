# coding=utf-8

from Elenco import comuni

# inizializzo il dizionario anagrafica
Anagrafica = {}

# inizializzo i dizionari di appoggio
Mesi = {
    "01": "A",
    "02": "B",
    "03": "C",
    "04": "D",
    "05": "E",
    "06": "H",
    "07": "L",
    "08": "M",
    "09": "P",
    "10": "R",
    "11": "S",
    "12": "T"
}

Dispari = {
    "0": "1",
    "1": "0",
    "2": "5",
    "3": "7",
    "4": "9",
    "5": "13",
    "6": "15",
    "7": "17",
    "8": "19",
    "9": "21",
    "A": "1",
    "B": "0",
    "C": "5",
    "D": "7",
    "E": "9",
    "F": "13",
    "G": "15",
    "H": "17",
    "I": "19",
    "J": "21",
    "K": "2",
    "L": "4",
    "M": "18",
    "N": "20",
    "O": "11",
    "P": "3",
    "Q": "6",
    "R": "8",
    "S": "12",
    "T": "14",
    "U": "16",
    "V": "10",
    "W": "22",
    "X": "25",
    "Y": "24",
    "Z": "23"
}

Pari = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "0",
    "B": "1",
    "C": "2",
    "D": "3",
    "E": "4",
    "F": "5",
    "G": "6",
    "H": "7",
    "I": "8",
    "J": "9",
    "K": "10",
    "L": "11",
    "M": "12",
    "N": "13",
    "O": "14",
    "P": "15",
    "Q": "16",
    "R": "17",
    "S": "18",
    "T": "19",
    "U": "20",
    "V": "21",
    "W": "22",
    "X": "23",
    "Y": "24",
    "Z": "25"
}

Resto = {
    "0": "A",
    "1": "B",
    "2": "C",
    "3": "D",
    "4": "E",
    "5": "F",
    "6": "G",
    "7": "H",
    "8": "I",
    "9": "J",
    "10": "K",
    "11": "L",
    "12": "M",
    "13": "N",
    "14": "O",
    "15": "P",
    "16": "Q",
    "17": "R",
    "18": "S",
    "19": "T",
    "20": "U",
    "21": "V",
    "22": "W",
    "23": "X",
    "24": "Y",
    "25": "Z"
}

# chiedo di inserire i dati
Anagrafica["Nome"] = input("Inserisci il nome: ").upper()
Anagrafica["Cognome"] = input("Inserisci il cognome: ").upper()
Anagrafica["Sesso"] = input("Inserisci il tuo sesso (M per maschio ed F per femmina): ").upper()
Anagrafica["Luogo"] = input("Inserisci il tuo luogo di nascita: ")
Anagrafica["Data"] = input("Inserisci la tua data di nascita (gg/mm/aaaa): ")


def consonanti(stringa, tipo):
    Consonanti = ["B", "C", "D", "F", "G", "H", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "Z"]
    mylist = [i for i in stringa if i in Consonanti]

    if tipo == "Nome":
        return mylist[0] + mylist[2] + mylist[3]
    else:
        return mylist[0] + mylist[1] + mylist[2]

def somma_alfa(stringa, dizionario):
    tot = 0
    for i in stringa:
        tot += int(dizionario[i])
    return tot

CF_Nome = consonanti(Anagrafica["Nome"], "Nome")

CF_Cognome = consonanti(Anagrafica["Cognome"], "Cognome")

CF_Anno = Anagrafica["Data"][-2:]

CF_Mese = Mesi[Anagrafica["Data"][3:5]]

if Anagrafica["Sesso"] == "M":
    CF_Sesso = 0
else:
    CF_Sesso = 40

CF_Giorno = str(int(Anagrafica["Data"][:2]) + CF_Sesso).zfill(2)

CF_Luogo = comuni.get(Anagrafica["Luogo"])

CF = CF_Cognome + CF_Nome + CF_Anno + CF_Mese + CF_Giorno + CF_Luogo

CF_Pari = [CF[i] for i in range(0, len(CF)) if i % 2 == 1]
CF_Dispari = [CF[i] for i in range(0, len(CF)) if i % 2 == 0]

CF_Controllo = Resto[str((somma_alfa(CF_Pari,Pari) + somma_alfa(CF_Dispari,Dispari)) % 26)]

CF += CF_Controllo

print("Il tuo codice fiscale è: ", CF)