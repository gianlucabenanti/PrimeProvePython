import pypyodbc
from configS import connect

class FMDBC():

    #metodo che restituisce la connection string in base alle impostazioni contenute nel file config
    def connection_string(self) -> str:
        return "DSN=" + connect["DSN"] + ";" + "Database=" + connect["Database"] + ";" + "UID=" + connect[
            "UID"] + ";" + "PWD=" + connect["PWD"] + ""

    #metodo che crea una connessione col database e restituisce un oggetto DB
    def connect(self, connection_string : str) -> "DB":
        return pypyodbc.connect(connection_string)

    #metodo che esegue una select
    def select(self, table : str, where : str, *fields : "args") -> list:
        x = ""

        #imposto la connection string ed eseguo la connessione
        DB = self.connect(self.connection_string())

        #imposto la stringa coi campi
        for listOfFields in fields:
            if x == "":
                x = listOfFields
            else:
                x = x + "," + listOfFields

        #imposto la clausula WHERE
        if where == "":
            wher = ""
        else:
            wher = " WHERE " + where

        #imposto la stringa con la query
        query = "SELECT " + listOfFields + " FROM " + table + wher

        #eseguo la query
        cursor = DB.cursor()
        cursor.execute( query )

        #memorizzo il risultato della query
        row = cursor.fetchall()

        #chiudo la connessione e il database
        cursor.close()
        DB.close()

        #restituisco il risultato
        return row

    #metodo che esegue una update
    def update(self, table : str, where : str, *updates : "args") -> list:
        x = ""

        #imposto la connection string ed eseguo la connessione
        DB = self.connect(self.connection_string())

        #imposto la stringa coi campi
        for listOfUpdates in updates:
            if x == "":
                x = " SET " + listOfUpdates
            else:
                x = x + "," + listOfUpdates

        #imposto la clausula WHERE
        if where == "":
            wher = ""
        else:
            wher = " WHERE " + where

        #imposto la stringa con la query
        query = "UPDATE " + table + x + wher

        #eseguo la query
        cursor = DB.cursor()
        cursor.execute( query )

        #eseguo il commit dei dati
        cursor.commit()

        #chiudo la connessione e il database
        cursor.close()
        DB.close()