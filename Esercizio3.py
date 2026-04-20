rubrica = {
  'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 46, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

#Punto 1
def punto1():
    print(f'Paolino Paperino è nato il {rubrica["Paolino Paperino"]["giorno"]} {rubrica["Paolino Paperino"]["mese"]} {rubrica["Paolino Paperino"]["anno"]}, ha {rubrica["Paolino Paperino"]["età"]} anni, è di sesso {rubrica["Paolino Paperino"]["sesso"]} e il suo indirizzo mail è {rubrica["Paolino Paperino"]["mail"]}')
    print(f'Ron Weasley è nato il {rubrica["Ron Weasley"]["giorno"]} {rubrica["Ron Weasley"]["mese"]} {rubrica["Ron Weasley"]["anno"]}, ha {rubrica["Ron Weasley"]["età"]} anni, è di sesso {rubrica["Ron Weasley"]["sesso"]} e il suo indirizzo mail è {rubrica["Ron Weasley"]["mail"]}')
    print(f'Ramona Flowers è nata il {rubrica["Ramona Flowers"]["giorno"]} {rubrica["Ramona Flowers"]["mese"]} {rubrica["Ramona Flowers"]["anno"]}, ha {rubrica["Ramona Flowers"]["età"]} anni, è di sesso {rubrica["Ramona Flowers"]["sesso"]} e il suo indirizzo mail è {rubrica["Ramona Flowers"]["mail"]}')
    print(f'Madoka Ayukawa è nata il {rubrica["Madoka Ayukawa"]["giorno"]} {rubrica["Madoka Ayukawa"]["mese"]} {rubrica["Madoka Ayukawa"]["anno"]}, ha {rubrica["Madoka Ayukawa"]["età"]} anni, è di sesso {rubrica["Madoka Ayukawa"]["sesso"]} e il suo indirizzo mail è {rubrica["Madoka Ayukawa"]["mail"]}')

#Punto 2
Lista_eta = []
def punto2():
    for persona in rubrica:
        Lista_eta.append(rubrica[persona]['età'])
    Lista_eta.sort(key=int)
    for persona in range(len(rubrica)):
        for chiave in rubrica:
            if rubrica[chiave]['età'] == Lista_eta[persona]:
                Lista_eta[persona] = chiave
    print(Lista_eta)

#Punto 3
def punto3():    
    Lista_eta_contrario = Lista_eta[::-1]
    print(Lista_eta_contrario)

#Punto 4
def punto4():
    for persona in rubrica:
        if rubrica[persona]['sesso'] == 'F':
            lettera = "a"
            print(f'Car{lettera} {persona}, \nsei nat{lettera} il {rubrica[persona]["giorno"]} di {rubrica[persona]["mese"]} del {rubrica[persona]["anno"]} e quindi a breve compirai {rubrica[persona]["età"]} anni.\nTi manderemo gli auguri a {rubrica[persona]["mail"]}')
        elif rubrica[persona]['sesso'] == 'M':
            lettera = "o"
            print(f'Car{lettera} {persona}, \nsei nat{lettera} il {rubrica[persona]["giorno"]} di {rubrica[persona]["mese"]} del {rubrica[persona]["anno"]} e quindi a breve compirai {rubrica[persona]["età"]} anni.\nTi manderemo gli auguri a {rubrica[persona]["mail"]}')

#Punto 5
import sys
args1 = sys.argv
def punto5():
    for persona in rubrica:
        print(f'{persona}: ')
        for chiave in args1[1:]:
            if chiave in ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']:
                print(f'{chiave}: {rubrica[persona][chiave]}')

#Punto 6
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-nome", nargs="*") 
parser.add_argument("-esercizio", nargs="*")  
args = parser.parse_args()
persona3 = args.nome
if args.nome:
    for persona in persona3:
        if persona in rubrica:
            if rubrica[persona]['sesso'] == 'F':
                lettera = "a"
                print(f'Car{lettera} {persona}, \nsei nat{lettera} il {rubrica[persona]["giorno"]} di {rubrica[persona]["mese"]} del {rubrica[persona]["anno"]} e quindi a breve compirai {rubrica[persona]["età"]} anni.\nTi manderemo gli auguri a {rubrica[persona]["mail"]}')
            elif rubrica[persona]['sesso'] == 'M':
                lettera = "o"
                print(f'Car{lettera} {persona}, \nsei nat{lettera} il {rubrica[persona]["giorno"]} di {rubrica[persona]["mese"]} del {rubrica[persona]["anno"]} e quindi a breve compirai {rubrica[persona]["età"]} anni.\nTi manderemo gli auguri a {rubrica[persona]["mail"]}')


#Punto 7
for esercizio in args.esercizio:
    if esercizio == "1":
        punto1()
    elif esercizio == "2":
        punto2()
    elif esercizio == "3":
        punto3()
    elif esercizio == "4":
        punto4()
    elif esercizio == "5":
        punto5()
