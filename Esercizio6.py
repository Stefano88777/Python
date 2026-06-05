import rubrica

#creo l'oggetto rubrica rb
rb = rubrica.Rubrica()

while True:

    azione = input("\nScegli un'azione (APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA, EXIT): ")

    if azione == "EXIT":
        print("Uscita dal programma. Arrivederci!")
        break

    elif azione == "APRI":
        rb.APRI()

    elif azione == "AGGIUNGI":
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
        
        rb.AGGIUNGI(nome, nuovo_contatto)

    elif azione == "RIMUOVI":
        nome = input("Inserisci il nome del contatto da rimuovere: ")
        rb.RIMUOVI(nome)

    elif azione == "STAMPA":
        nome = input("Inserisci il nome del contatto da stampare: ")
        rb.STAMPA(nome)

    elif azione == "SALVA":
        nome_file = input("Inserisci il nome del file su cui salvare: ")
        rb.SALVA(nome_file)

    else:
        print("Azione non esistente. Riprova.")