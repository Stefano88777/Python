#EAFP= easier ask forgiveness than permission
import json
import random

file = open("parole.json", "r")
dati = file.read()
lista_parole = json.loads(dati)

parola_segreta = random.choice(lista_parole)
lettere_provate = []
vite = 6

while vite > 0:
    parola_visualizzata = ""
    for lettera in parola_segreta:
        if lettera in lettere_provate:
            parola_visualizzata = parola_visualizzata + lettera
        else:
            parola_visualizzata = parola_visualizzata + "_"
            
    print("Parola: " + parola_visualizzata)
    print("Vite rimaste: " + str(vite))
    
    scelta = input("Inserisci una lettera o indovina la parola: ").lower()
    
    try:
        #se indovina la parola intera, usciamo subito dal gioco
        if scelta == parola_segreta:
            print("Hai indovinato la parola intera")
            break
            
        #se si inserisce un'altra parola, lanciamo un errore per andare nell'except
        if len(scelta) != 1:
            raise ValueError

        #se i due casi sono falliti significa che ha inserito una lettera
        lettere_parola = list(parola_segreta)
        
        #proviamo a rimuovere la lettera dalla lista delle lettere della parola, se non riusciamo finiamo di nuovo in un ValueError
        lettere_parola.remove(scelta)
        
        #altrimenti la lettera e' corretta
        lettere_provate.append(scelta)
        print("Lettera corretta")
        
    except ValueError:
        print("Sbagliato")
        vite = vite - 1

    if "_" not in parola_visualizzata:
        print("Hai vinto")
        break

if vite == 0:
    print("Hai perso! La parola era: " + parola_segreta)