
def generatore_di_tabelline(numero):
    """generatore infinito di multipli di un numero"""
    n = 0
    
    while True:
        yield n*numero
        n=n+1
        
x = input('Con quale tabellina vuoi giocare?')

#controllo se l'input iniziale contiene caratteri strani
valido = True
for carattere in x:
    if carattere not in '0123456789':
        valido = False

while x == "" or valido == False:
    print("Non hai inserito un numero intero valido")
    x = input('Con quale tabellina vuoi giocare? ')
    valido = True
    for carattere in x:
        if carattere not in '0123456789':
            valido = False

x_int = int(x)

print(f'Giocheremo con il numero {x_int}')
g = generatore_di_tabelline(x_int)
numero_tabellina=next(g)

continua = True

while continua:
    prossimo_numero = next(g)
    
    guess = input(f'Il numero attuale è {numero_tabellina}. Quale è il prossimo numero? ')
    
    #controllo se fermare il gioco
    if guess == 'FINE':
        continua = False
    else:
        #Controllo se la risposta contiene lettere, decimali o simboli
        risposta_valida = True
        for carattere in guess:
            if carattere not in '0123456789':
                risposta_valida = False

        if guess != "" and risposta_valida == True:
            guess = int(guess)
            #Controllo se l'utente ha indovinato il numero calcolato dal generatore
            if prossimo_numero == guess:
                print('hai indovinato')
                numero_tabellina = prossimo_numero  #Aggiorno il numero corrente
            else:
                print('riprova')
        else:
            print('Hai inserito lettere, decimali o caratteri speciali, riprova...'/n)

print('Esco dal gioco')