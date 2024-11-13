vendite_reparto=(
    ("Informatica", [("gennaio", 1000),("febbraio", 235),("marzo", 12),("aprile", 453),("maggio", 864),("giugno", 123) ]),
    ("Cibo", [("gennaio", 1000),("febbraio", 235),("marzo", 10453),("aprile", 5),("maggio", 1250),("giugno", 2425) ]),
    ("Elettronica", [("gennaio", 1231),("febbraio", 34),("marzo", 1246),("aprile", 39),("maggio", 36),("giugno", 89) ]),
    ("Frutta", [("gennaio", 458),("febbraio", 1234),("marzo", 4321),("aprile", 456),("maggio", 987),("giugno", 4346) ]) 
    )

def media_vendite(reparto):
    max=0
    min=100000
    somma=0
    c=0
    for reparto,dati in vendite_reparto:
         if nuovo_reparto==reparto: 
            for mese,valore in dati:
                if valore>max:
                    max=valore
                    meseMax=mese
                elif valore<min :
                    min=valore
                    meseMin=mese
                if valore!="N/D" :
                    somma+=valore
                    c+=1
    media_totale=somma/c                          
    print(media_totale,(max,meseMax),(min,meseMin))


nuovo_reparto=input("inserisci un reparto da analizzare: ")
media_vendite(nuovo_reparto)