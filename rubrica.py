import json

class Rubrica:
    def __init__(self):
        self.data = {
            'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93, 'sesso': 'M', 'mail': 'paolino.paperino@disney.org'},
            'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
            'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona@flowers.com'},
            'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka@ayukawa.jp'}
        }
        self.aperta = True

    #se il file con cui lavoriamo e' json usaimo questo classmethod
    @classmethod
    def da_json(cls, nome_del_file):
        oggetto_rubrica = Rubrica()
        with open(nome_del_file, 'r') as file_in:
            oggetto_rubrica.data = json.load(file_in)
        oggetto_rubrica.aperta = True
        return oggetto_rubrica
    #se e' txt questo
    @classmethod
    def da_testo(cls, nome_del_file):
        oggetto_rubrica = Rubrica()
        oggetto_rubrica.data = {}
        with open(nome_del_file, 'r') as file_in:
            for linea in file_in:
                if ":" in linea:
                    parti = linea.strip().split(":")
                    nome = parti[0]
                    #salvo i dati
                    oggetto_rubrica.data[nome] = parti[1]
        oggetto_rubrica.aperta = True
        return oggetto_rubrica

    #funzione che apre un file
    def apri(self, nome_del_file=None):
        if nome_del_file is None:
            nome_del_file = input("Inserisci il nome del file da aprire: ")
        
        with open(nome_del_file, 'r') as file_in:
            #o json
            if nome_del_file.endswith('.json'):
                self.data = json.load(file_in)
            #o di testo
            else:
                self.data = {}
                for linea in file_in:
                    if ":" in linea:
                        parti = linea.strip().split(":")
                        self.data[parti[0]] = parti[1]
        self.aperta = True
        print(f"File {nome_del_file} aperto.")

    #funzione che aggiunge un elemento al dizionario
    def aggiungi(self, nome, info_dizionario):
        if self.aperta == False:
            print("Prima apri una rubrica")
            return
        self.data[nome] = info_dizionario
        print(f"Contatto {nome} aggiunto.")

    #funzione che rimuove un elemento dal dizionario
    def rimuovi(self, nome):
        if len(self.data) == 0:
            print("La rubrica è vuota")
            return
        if nome not in self.data:
            print(f"Il contatto {nome} non esiste in rubrica")
            return
        del self.data[nome]
        print(f"Contatto {nome} rimosso.")

    #funzione che visualizza un elemento
    def stampa(self, nome):
        if len(self.data) == 0:
            print("La rubrica è vuota")
            return
        if nome not in self.data:
            print(f"Il contatto {nome} non esiste in rubrica")
            return
        
        dati = self.data[nome]
        
        print(f"\nCiao {nome},")
        print(f"sei nat[o/a] il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni.")
        print(f"Ti manderemo gli auguri a {dati['mail']}\n")

    #funzione che salva il file
    def salva(self, nome_del_file):
        if len(self.data) == 0:
            print("La rubrica è vuota")
            return
        
        if nome_del_file.endswith('.json'):
            with open(nome_del_file, 'w') as file_out:
                json.dump(self.data, file_out, indent=4)
        else:
            with open(nome_del_file, 'w') as file_out:
                for nome in self.data:
                    file_out.write(f"{nome}:{self.data[nome]}\n")
        print(f"Rubrica salvata in {nome_del_file}")