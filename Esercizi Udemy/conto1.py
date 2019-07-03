class Conto:

    def __init__(self,nome,conto):
        self.nome = nome
        self.conto = conto

class ContoCorrente(Conto):

    def __init__(self,nome,conto,importo):
        super().__init__(nome,conto)
        self.__saldo = importo

    def preleva(self,importo):
        self.__saldo -= importo

    def deposita(self,importo):
        self.__saldo += importo

    def descrizione(self):
        print('Questo conto è intestato a: ', self.nome,'\nIl numero di conto è: ',self.conto, '\nIl saldo disponibile è: ', self.saldo, '\n')

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,importo):
        self.preleva(self.saldo)
        self.deposita(importo)

class GestoreContiCorrenti:

    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)

C1 = ContoCorrente('Gianluca','0001',1549)
C2 = ContoCorrente('Daniele','0002',2897)

C1.descrizione()
C2.descrizione()

GestoreContiCorrenti.bonifico(C1,C2,100)

C1.descrizione()
C2.descrizione()