def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

fname = "C:/Gianluca/PYTHON/Elenco.csv"

f = open(fname,"r")

stringa = f.readlines()

f.close()

dict = {stringa[i][:stringa[i].find(";")]:stringa[i][stringa[i].find(";")+1:] for i in range(0,file_len(fname))}


f = open("C:/Gianluca/PYTHON/DizionarioComuni.py","a")

f.write(str(dict))

f.close()