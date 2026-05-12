
def generatore_di_tabelline(numero):
    """generatore infinito di multipli di un numero"""
    n = 0
    
    while True:
        yield n*numero
        n=n+1
        
x = input('Con quale tabellina vuoi giocare?')
x_int = int(x)

print(f'Giocheremo con il numero {x_int}')
g = generatore_di_tabelline(x_int)
numero_tabellina=next(g)

continua = True

while continua:
    
    guess = input(f'Il numero attuale è {numero_tabellina}. Quale è il prossimo numero?')
    
    #controllo se fermare il gioco
    if guess == 'FINE':
        continua = False
    else:
        guess = int(guess)
        numero_tabellina = next(g)
        if numero_tabellina == guess:
            print('hai indovinato')
        else:
            print('riprova')

print('Esco dal gioco')

