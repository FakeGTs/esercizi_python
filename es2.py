#Dati dei corsi organizzati in diverse citta
corsi = (
    ("Milano", [
        ("gennaio", ("online", 50)),
        ("gennaio", ("in presenza", 30)),
        ("febbraio", ("online", 40)),
        ("febbraio", ("in presenza", 25)),
        ("marzo", ("online", 30)),
        ("marzo", ("in presenza", 30)),
    ]),
    ("Bologna", [
        ("gennaio", ("online", 45)),
        ("gennaio", ("in presenza", 20)),
        ("febbraio", ("online", 35)),
        ("febbraio", ("in presenza", 30)),
        ("marzo", ("online", 80)),
        ("marzo", ("in presenza", 10)),    
    ]),
    ("Roma", [
        ("gennaio", ("online", 45)),
        ("gennaio", ("in presenza", 20)),
        ("febbraio", ("online", 35)),
        ("febbraio", ("in presenza", 30)),
        ("marzo", ("online", 60)),
        ("marzo", ("in presenza", 70)),    
    ]),
)

def analizza_partecipanti(cittaScelta,modalitaScelta):
    for citta, dati in corsi:
        if citta==cittaScelta:
            partecipanti_totali=0
            conta=0
            max_partecipanti=0
            mese_max_partecipanti=""
            for mese, (modalita, partecipanti) in dati:
                if modalitaScelta==modalita:
                    partecipanti_totali+=partecipanti
                    conta+=1
                    if partecipanti>max_partecipanti:
                        max_partecipanti=partecipanti
                        mese_max_partecipanti=mese        
            if conta>0:
                media_partecipanti=partecipanti_totali/conta  
                print (round(media_partecipanti,1),(max_partecipanti, mese_max_partecipanti))
            else:
                return (0, (0, "nessun mese"))

cittaScelta=input("Scegli una citta: ")
modalita=input("Scegli una modalita: ")
analizza_partecipanti(cittaScelta,modalita)