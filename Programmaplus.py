import json
import random
import time

print("Simulatore di lanci con un dado")

#chiedo quanti lanci eseguire e controllo che non vengano inseriti caratteri non validi
while True:
    risposta = input("Quanti lanci vuoi simulare? ")
    try:
        n_lanci = int(risposta) 
        if n_lanci > 0:
            print(f"\nSto lanciando il dado {n_lanci} volte...")
            break  
        else:
            print("Inserisci un numero maggiore di 0!")
    except ValueError:
        print("Errore: Inserisci un numero intero valido.")

cronologia_lanci = []
possibilita = [1, 2, 3, 4, 5, 6]
#calcolo il tempo necessario
tempo_inizio = time.time()

for i in range(n_lanci):
    lancio = random.choice(possibilita)
    cronologia_lanci.append(lancio)

tempo_fine = time.time()
tempo_totale = tempo_fine - tempo_inizio

contatore_facce = [0, 0, 0, 0, 0, 0]
for i in range(1, 7):
    #per ogni numero da 1 a 6 conto quante volte si presenta nella cronologia
    for x in range(len(cronologia_lanci)):
        if cronologia_lanci[x] == i:
            contatore_facce[i - 1] = contatore_facce[i - 1] + 1

faccia1 = contatore_facce[0]
faccia2 = contatore_facce[1]
faccia3 = contatore_facce[2]
faccia4 = contatore_facce[3]
faccia5 = contatore_facce[4]
faccia6 = contatore_facce[5]

#uso una list comprehension per contare il numero di uscite di 5 e 6
lanci_alti = [lancio for lancio in cronologia_lanci if lancio > 4]
quanti_alti = len(lanci_alti)

#calcolo la media e le percentuali
media_risultati = sum(cronologia_lanci) / len(cronologia_lanci)

percentuale_1 = (faccia1 / n_lanci) * 100
percentuale_2 = (faccia2 / n_lanci) * 100
percentuale_3 = (faccia3 / n_lanci) * 100
percentuale_4 = (faccia4 / n_lanci) * 100
percentuale_5 = (faccia5 / n_lanci) * 100
percentuale_6 = (faccia6 / n_lanci) * 100

maggiore_uscita = max(faccia1, faccia2, faccia3, faccia4, faccia5, faccia6)
minore_uscita = min(faccia1, faccia2, faccia3, faccia4, faccia5, faccia6)

print(f" Tempo impiegato: {tempo_totale:.3f} secondi")
print(f" Media ottenuta: {media_risultati:.3f}")
print(f" Totale lanci fortunati (5 o 6): {quanti_alti} su {n_lanci}")

#salvo i dati in un file JSON
statistiche = {
    "lanci_totali": n_lanci,
    "tempo_calcolo_secondi": round(tempo_totale, 5),
    "media_punti_dado": round(media_risultati, 4),
    "totale_lanci_alti_5_6": quanti_alti,
    "volte_faccia_1": faccia1, "volte_faccia_2": faccia2, "volte_faccia_3": faccia3,
    "volte_faccia_4": faccia4, "volte_faccia_5": faccia5, "volte_faccia_6": faccia6,
    "percentuale_faccia_1": round(percentuale_1, 2), "percentuale_faccia_2": round(percentuale_2, 2),
    "percentuale_faccia_3": round(percentuale_3, 2), "percentuale_faccia_4": round(percentuale_4, 2),
    "percentuale_faccia_5": round(percentuale_5, 2), "percentuale_faccia_6": round(percentuale_6, 2),
    "record_massimo_lanci": maggiore_uscita,
    "record_minimo_lanci": minore_uscita
}

with open("statistiche_dado.json", "w") as file_json:
    json.dump(statistiche, file_json, indent=4)
