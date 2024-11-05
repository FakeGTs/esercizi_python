dati= (
    ("Milano", [("Gennaio", 1.1),("Febbraio", 2.3), ("Marzo", 1.1),("Aprile", 0.0),("Maggio", 1.1),("Giugno", 5.3),("Luglio", 0.1),("Agosto", 2.3),("Settembre", 8.1),("Ottobre", 3.3),("Novembre", 1.4),("Dicembre", 20.3)]),
    ("Monza", [("Gennaio", 1.6),("Febbraio", 2.0), ("Marzo", 1.5),("Aprile", 0.3),("Maggio", 1.1),("Giugno", 3.3),("Luglio", 1.5),("Agosto", 2.2),("Settembre", 2.1),("Ottobre", 9.3),("Novembre", 7.1),("Dicembre", 0.0)]),
    ("Varese", [("Gennaio", 0.2),("Febbraio", 0.3), ("Marzo", 1.7),("Aprile", 2.6),("Maggio", 1.1),("Giugno", 2.9),("Luglio", 3.1),("Agosto", 2.6),("Settembre", 7.1),("Ottobre", 2.5),("Novembre", 1.2),("Dicembre", 2.4)]),
    ("Bergamo", [("Gennaio", 1.9),("Febbraio", 9.4), ("Marzo", 1.0),("Aprile", 1.3),("Maggio", 1.1),("Giugno", 7.3),("Luglio", 0.1),("Agosto", 2.3),("Settembre", 2.1),("Ottobre", 4.2),("Novembre", 4.1),("Dicembre", 0.3)])
)

def calcola_temperatura_media(citta, dati):
    dati_citta = []

    for nome_citta, rilevazioni in dati:
        if nome_citta == citta:
            for mese,rilevazione in rilevazioni:
                if(rilevazione!="N/D"):
                 dati_citta.append(rilevazione)

    if not dati_citta:
        return None

    temp_media = sum(dati_citta) / len(dati_citta)
    temp_max = max(dati_citta)
    meseMax=0
    temp_min = min(dati_citta)
    meseMin=0
    return (temp_media, temp_max, temp_min)

for citta, temp in dati:
    risultato = calcola_temperatura_media(citta, dati)
    if risultato:
        print(f"{citta}: Val media = {round(risultato[0],2)}, Val max = {risultato[1]}, Val min = {risultato[2]}")
    else:
        print(f"Nessun dato disponibile per {citta}")