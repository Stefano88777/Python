
def is_pari(n):
    risultato = True
    if n%2 == 1:
       risultato = False
    return risultato

def genera_numeri():       
    numero=int(input('\nDammi un numero intero positivo:  '))
    if numero > 0:
        return is_pari(numero), numero
    else:
        return genera_numeri()

def crea_lista(n, lista):
    lista.append(n)
    if n==1 or len(lista)==100:
        return lista
    else:
        if is_pari(n)==True:
            n=n//2
            return crea_lista(n, lista)
        else:
            n=(n*3)+1
            return crea_lista(n, lista)

def analizza_sequenza(n):
    massimo=max(n)
    somma=sum(n)
    lunghezza=len(n)
    return massimo, somma, lunghezza

def ricerca_lista(n):
    multipli=[]
    for x in n:
        if x%5 == 0:
            multipli.append(x)
    if multipli==[]:
        return 'Non ci sono multipli di 5'
    else:
        numeri='I multipli di 5 sono: ' + str(multipli)
        return numeri

def main():
    result, numero = genera_numeri()
    print(result)
    lista_finale = crea_lista(numero, [])
    print(lista_finale)
    massimo, somma, lunghezza = analizza_sequenza(lista_finale)
    print('Il valore massimo della lista è:', massimo)
    print('La somma dei valori nella lista è:' , somma)
    print('La sua lunghezza è:' , lunghezza)
    ricerca=ricerca_lista(lista_finale)
    print (ricerca)
    return numero, lunghezza
x=int(input('Quanti numeri volete analizzare: '))
for i in range(x):
    numero, lunghezza = main()
    lunghezza_base = 0
    miglior_numero = None
    if lunghezza > lunghezza_base:
        lunghezza_base=lunghezza
        miglior_numero=numero
print('\nRIEPILOGO FINALE:')
print('Il numero con la sequenza più lunga è: ' , miglior_numero)
print('La sua lunghezza è: ' , lunghezza_base)