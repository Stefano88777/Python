import rubrica

#creo l'oggetto rubrica rb
rb = rubrica.Rubrica()

while True:

    azione = input("\nScegli un'azione (apri, aggiungi, rimuovi, salva, stampa, exit): ")

    if azione == "exit":
        print("Uscita dal programma. Arrivederci!")
        break

    elif azione == "apri":
        rb.apri()

    elif azione == "aggiungi":
        nome = input("Inserisci il nome del contatto: ")
        giorno = input("Giorno di nascita: ")
        mese = input("Mese di nascita: ")
        anno = input("Anno di nascita: ")
        eta = input("Età: ")
        sesso = input("Sesso (M/F): ")
        mail = input("Email: ")
        
        nuovo_contatto = {
            'giorno': giorno,
            'mese': mese,
            'anno': anno,
            'età': eta,
            'sesso': sesso,
            'mail': mail
        }
        
        rb.aggiungi(nome, nuovo_contatto)

    elif azione == "rimuovi":
        nome = input("Inserisci il nome del contatto da rimuovere: ")
        rb.rimuovi(nome)

    elif azione == "stampa":
        nome = input("Inserisci il nome del contatto da stampare: ")
        rb.stampa(nome)

    elif azione == "salva":
        nome_file = input("Inserisci il nome del file su cui salvare: ")
        rb.salva(nome_file)

    else:
        print("Azione non esistente. Riprova.")