import threading
import socket
import mysql.connector
import sys

comunicazioni = ["", ""]
PASSWORD = "CIAO"


def gestisci_comunicazione(conn):
    conn.send("Benvenuto, inserisci password: ".encode())
    data = conn.recv(1024).decode()
    i = 0
    while data != PASSWORD and i < 2:
        i += 1
        conn.send(f"Password ERRATA, reinserisci password: tentativi rimasti {3 - i} ".encode())
        data = conn.recv(1024).decode()

    if (data != PASSWORD):
        conn.send("STOP".encode())
        conn.close()
        return

    while True:
        conn.send("Benvenuto, cosa vuoi fare: i=insert, u=update, r=read, d=delete, e=exit".encode())
        data = conn.recv(1024).decode()
        print(data)

        if (data == "r"): #READ
            conn.send("su che tabella vuoi cercare: c=clienti, z=zone di lavoro".encode())
            data = conn.recv(1024).decode()
            dati_query = db_get(data)
            print("i dati della tabella sono: ", dati_query)

        elif (data == "d"): #DELETE
            conn.send("su che tabella vuoi eliminare: c=clienti, z=zone di lavoro".encode())
            data = conn.recv(1024).decode()
            dati_query = db_delete(conn, data)
            print(dati_query)

        elif(data == "i"): #INSERT
            conn.send("su che tabella vuoi inserire: c=clienti, z=zone di lavoro".encode())
            data = conn.recv(1024).decode()

            dati_query = db_insert(conn, data)
            print(dati_query)

        if (data == "u"): #UPDATE
            conn.send("su che tabella vuoi aggiornare: c=clienti, z=zone di lavoro".encode())
            data = conn.recv(1024).decode()

            db_update(conn, data)

        if (data == "e"): #EXIT
            conn.send("arrivederci".encode())
            sys.exit()


#SELECT ##################################################################################################
def db_get(scelta):
    cono = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="5ATepsit",
        port=3306,
    )
    cur = cono.cursor()

    if scelta == "c":
        query = "SELECT * FROM dipendenti_erika_boccadoro"
        cur.execute(query)
        dati = cur.fetchall()
    
    elif scelta == "z":
        query = "SELECT * FROM zone_di_lavoro_boccadoro_erika"
        cur.execute(query)
        dati = cur.fetchall()
    
    return dati


#DELETE ##################################################################################################
def db_delete(conn, scelta):
    cono = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="5ATepsit",
        port=3306,
    )
    cur = cono.cursor()

    if scelta == "c":
        conn.send("quale nome vuoi eleminare: ".encode())
        elim = conn.recv(1024).decode()

        query = f"DELETE FROM `dipendenti_erika_boccadoro` WHERE nome = '{elim}'"
        cur.execute(query)
        cono.commit()
    
    elif scelta == "z":
        conn.send("quale id vuoi eleminare: ".encode())
        elim = conn.recv(1024).decode()

        query = f"DELETE FROM `zone_di_lavoro_boccadoro_erika` WHERE id_zona = '{elim}'"
        cur.execute(query)
        cono.commit()

    return



#INSERT ##################################################################################################
def db_insert(conn, scelta):
    cono = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="5ATepsit",
        port=3306,
    )
    cur = cono.cursor()

    if scelta == "c":
        conn.send("inserisci il nome del nuovo dipendente: ".encode())
        n = conn.recv(1024).decode()
        nome= str(n)
        conn.send("inserisci il cognome del nuovo dipendente: ".encode())
        c = conn.recv(1024).decode()
        cognome=str(c)
        conn.send("inserisci la posizione lavorativa del nuovo dipendente: ".encode())
        pos = conn.recv(1024).decode()
        posizione_lavorativa = str(pos)
        conn.send("inserisci la data di assunzione del nuovo dipendente: ".encode())
        data_ass = conn.recv(1024).decode()
        data_assunzione = str(data_ass)
        conn.send("inserisci la data di nascita del nuovo dipendente: ".encode())
        data_n = conn.recv(1024).decode()
        data_nascita = str(data_n)
        conn.send("inserisci la mail del nuovo dipendente: ".encode())
        m = conn.recv(1024).decode()
        mail = str(m)

        query = f"INSERT INTO `dipendenti_erika_boccadoro` (`id`, `nome`, `cognome`, `posizione_lavorativa`, `data_assunzione`, `data_nascita`, `mail`) VALUES ('', '{nome}', '{cognome}', '{posizione_lavorativa}', '{data_assunzione}', '{data_nascita}', '{mail}')"

        cur.execute(query)
        cono.commit()


    elif scelta == "z":
        conn.send("inserisci il nome della nuova zona: ".encode())
        n = conn.recv(1024).decode()
        nome= str(n)
        conn.send("inserisci il numero dei clienti: ".encode())
        num = conn.recv(1024).decode()
        numero_clienti=str(num)
        conn.send("inserisci l'id del dipendente che lavora in quella zona: ".encode())
        id_d = conn.recv(1024).decode()
        id_dipendente = str(id_d)
        conn.send("inserisci il progetto che sta svolgendo la zona: ".encode())
        prog = conn.recv(1024).decode()
        progetto_zona = str(prog)

        query = f"INSERT INTO `zone_di_lavoro_boccadoro_erika` (`id_zona`, `nome_zona`, `numero_clienti`, `id_dipendente`, `progetto_zona`) VALUES ('', '{nome}', '{numero_clienti}', '{id_dipendente}', '{progetto_zona}')"

        cur.execute(query)
        cono.commit()
    
    return



#UPDATE ##################################################################################################
def db_update(conn, scelta):
    cono = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="5ATepsit",
        port=3306,
    )
    cur = cono.cursor()

    if scelta == "c":
        conn.send("inserisci l'id del dipendente che vuoi modificare: ".encode())
        id_mod = conn.recv(1024).decode()
        id_modifica ="id = "
        id_modifica = id_modifica + "'" + str(id_mod) + "'"

        conn.send("quale parametro vuoi aggiornare? id, nome, cognome, pos_lav, data_nasc, data_assunz, email".encode())
        agg = conn.recv(1024).decode()
        parametro = f"{agg} = "
        
        conn.send("scrivi la modifica: ".encode())
        mod= conn.recv(1024).decode()
        parametro = parametro + "'" + str(mod) + "'"

        query = (f"UPDATE dipendenti_erika_boccadoro SET {parametro} WHERE {id_modifica}")

        print(query)

        cur.execute(query)
        cono.commit()

    elif scelta == "z":
        conn.send("inserisci l'id della zona che vuoi modificare: ".encode())
        id_mod = conn.recv(1024).decode()
        id_modifica ="id_zona = "
        id_modifica = id_modifica + "'" + str(id_mod) + "'"

        conn.send("quale parametro vuoi aggiornare? id_zona, nome_zona, numero_clienti, id_dipendente, progetto_zona".encode())
        agg = conn.recv(1024).decode()
        parametro = f"{agg} = "
        
        conn.send("scrivi la modifica: ".encode())
        mod= conn.recv(1024).decode()
        parametro = parametro + "'" + str(mod) + "'"

        query = (f"UPDATE zone_di_lavoro_boccadoro_erika SET {parametro} WHERE {id_modifica}")

        print(query)

        cur.execute(query)
        cono.commit()

    return


#MAIN #########################################################################################################
print("server in ascolto: ")
lock = threading.Lock()
HOST = ''  # Nome simbolico che rappresenta il nodo locale, ci va l'indirizzo IP
PORT = 50010  # Porta non privilegiata arbitraria
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
thread = []
lista_connessioni = []
i = 0

while True:
    lista_connessioni.append(s.accept())  # connessione = s.accept()
    print('Connected by', lista_connessioni[i][1])  # print(connessione[0])
    thread.append(threading.Thread(target=gestisci_comunicazione, args=(lista_connessioni[i][0],)))
    thread[i].start()
    i += 1