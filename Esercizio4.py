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
#apre un file rubrica.txt e scrive dentro i dati per ogni persona
file_testo = open('rubrica.txt', 'w')
for persona in rubrica:
    file_testo.write(f'{persona}, {rubrica[persona]["giorno"]},{rubrica[persona]["mese"]},{rubrica[persona]["anno"]},{rubrica[persona]["età"]},{rubrica[persona]["sesso"]},{rubrica[persona]["mail"]}\n')
file_testo.close()

import json
#crea un file json con la rubrica
with open("data_file.json", "w") as write_file:
    json.dump(rubrica, write_file)
#stampa la rubrica a schermo
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print(data)