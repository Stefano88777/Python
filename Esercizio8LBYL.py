#LBYL=look before you leap
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
    #verifico se e' stata inserita una lettera o una parola con if/else e se quest'ultima e' giusta o sbagliata
    if len(scelta) == 1:
        lettere_provate.append(scelta)
        if scelta in parola_segreta:
            print("Lettera corretta")
        else:
            print("Lettera sbagliata")
            vite = vite - 1
    else:
        if scelta == parola_segreta:
            print("Hai indovinato la parola")
            break
        else:
            print("Parola sbagliata")
            vite = vite - 1
            
    if "_" not in parola_visualizzata:
        print("Hai vinto")
        break

if vite == 0:
    print("Hai perso! La parola era: " + parola_segreta)