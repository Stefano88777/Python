#
# File: Otto_regine.py
#
# Author: E.Romelli, D.Tavagnacco
#
# Date: 2026/04/14
#
# Version: 1.0
#
# Description: Example program to solve 8 queen-like problem 
#              using brute force + random approach
#


def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    # distanza lungo y
    dy = abs(y1 - y0)
    
    # distanza lungo x
    dx = abs(x1 - x0) 

    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression
    return dx == dy     


def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti 
    '''
    # controllo tutte le precedenti fino a questa 'col'
    for c in range(col):     
        # la coordinata X (la riga) è indice (c) 
        # la coordinata Y,(la colonna) è valore lista nell'indice (c)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            # stop se trovo problemi
            return True  
    # nessun incrocio, la posizione va bene e NON incrocia altre colonne        
    return False   


def soluzione_ok(soluzione_posizioni):
    '''Controlla tutte le posizioni della possibile soluzione
       'soluzione_posizioni' per verificare se ognuna delle posizioni 
       (colonne dela permatazione) ogni colonna incrocia la diagonale
       di qualche altra posizione
    '''

    for col in range(1, len(soluzione_posizioni)):
        # verifica se incrocia
        #if incrocia_colonne(soluzione_posizioni, col) == True:
        if incrocia_colonne(soluzione_posizioni, col):
            # stop se trova incroci, la soluzione non è valida
            return False 

    # Se non è ritornato prima, 
    # allora nessun incrocio trvato: posizioni della soluzione valide 
    return True 

#Punto7
def soluzioni_uniche(scacchiera, n):
    #creo le altre quattro soluzioni e poi le andro a inserire in un dizionario per verificare se sono gia apparse
    lista_coordinate = []
    novanta_gradi = []
    centoottanta_gradi = []
    duecentosettanta_gradi = []
    x = 0
    for c in scacchiera:
        #scrivendo alcuni casi su carta ho notato che ruotando la scacchiera di novanta gradi, la colonna diventa la nuova riga e la nuova colonna e' n-c(-1 perche si conta da 0)
        lista_coordinate.append([c,x])
        novanta_gradi.append([x, n-1-c])
        centoottanta_gradi.append([n-1-c, n-1-x])
        duecentosettanta_gradi.append([n-1-x, c])
        x = x + 1
    return lista_coordinate, novanta_gradi, centoottanta_gradi, duecentosettanta_gradi

import random
import time 

def main(n=8, max_soluzioni=10):
    # inizializzo generatore permutazioni
    random_generator = random.Random() 
    # preparo la "possibile soluzione" con posizoni da testare
    scacchiera = list(range(n)) 
    #generalizziamo a NxN e verifichiamo i problemi di soluzioni massime per evitare loop infiniti
    if n in {1, 4, 6}: 
        max_soluzioni = 1
    elif n in {2, 3}:
        print(f'Non ci sono soluzioni')
        return 0.0, {}
    elif n == 7:
        max_soluzioni = 6
    # conto le soluzioni trovate, inizio da 0           
    solutions = 0                 
    tentativi = 0
    ripetizioni = 1
    lista_di_soluzioni = []
    dizionario_soluzioni = {}
    lista_rotazioni = []
    # misuro il tempo di partenza per la ricerca della soluzione
    start_time = time.time()            
    start_time2 = time.time()
    # loop finchè non trovo una soluzione
    while solutions < max_soluzioni:
    
        # permutazione casuale della soluzione 'mescolando' posizioni
        random_generator.shuffle(scacchiera) 
        
        # verifica se la permutazione casuale e' soluzione  
        #if soluzione_ok(scacchiera) == True: 
        if soluzione_ok(scacchiera) : 
            scacchiera_tupla = tuple(scacchiera)
            rotazioni = soluzioni_uniche(scacchiera, n)
            rot_0 = sorted(rotazioni[0])
            rot_90 = sorted(rotazioni[1])
            rot_180 = sorted(rotazioni[2])
            rot_270 = sorted(rotazioni[3])
            if rot_0 not in lista_rotazioni or rot_90 not in lista_rotazioni or rot_180 not in lista_rotazioni or rot_270 not in lista_rotazioni:
                lista_rotazioni.append(rot_0)
                lista_rotazioni.append(rot_90)
                lista_rotazioni.append(rot_180)
                lista_rotazioni.append(rot_270)
                if scacchiera_tupla not in dizionario_soluzioni:
                    #Punto 4, controllo le ripetizioni
                    dizionario_soluzioni[scacchiera_tupla] = 1
                else:
                    dizionario_soluzioni[scacchiera_tupla] = dizionario_soluzioni[scacchiera_tupla] + 1
                if scacchiera_tupla not in lista_di_soluzioni:                          #Punto 3, controllo l'unicita' delle soluzioni
                    tempo_usato = time.time() - start_time
                    print(f'Found solution {scacchiera} in {tempo_usato} s.')
                    print(f'Tentativi = {tentativi}')
                    # incremento contatore soluzioni trovate (condizione stop loop)     
                    solutions = solutions + 1
                    tentativi = 0
                    lista_di_soluzioni.append(scacchiera_tupla)
                    # reset timer ricerca soluzione
                    start_time = time.time()
        else:
            tentativi = tentativi + 1
    

    tempo_medio = (time.time() - start_time2) / max_soluzioni
    return tempo_medio, dizionario_soluzioni, lista_rotazioni
    

# chiamo la funzione principale 
n = int(input("Inserisci la dimensione della scacchiera: "))
max_soluzioni = int(input("Inserisci il numero massimo di soluzioni da cercare: "))
tempo_medio, dizionario_soluzioni, lista_rotazioni = main(n, max_soluzioni)
print(f'Il tempo medio è {tempo_medio}')
print('Ripetizioni soluzioni: ', dizionario_soluzioni)
print('Lista delle soluzioni e loro rotazioni: ', lista_rotazioni)
#Punto6
tempo_tentativo = 0
n = 8
continua = True
while continua:
    if tempo_tentativo < 15:
        n = n + 1
        tempo_tentativo,_,_ = main(n, 1)
    else:
        continua = False
print(f'Il numero massimo di colonne per il quale si trova una soluzione in meno di 15 secondi è {n-1}')

