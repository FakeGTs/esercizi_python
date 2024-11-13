tupla_pluviometrica = (
                      (("Vittuone","Milano"),(2022, ("gennaio",20))),
                      (("Vittuone","Milano"),(2023, ("marzo",80))),
                      (("Vittuone","Milano"),(2023, ("aprile",60))),
                      (("Vittuone","Milano"),(2023, ("maggio",80))),
                      (("Vittuone","Milano"),(2023, ("luglio",30))),
                      (("Vittuone","Milano"),(2023, ("agosto","N/D"))),
                      (("Varenna","Lecco"),(2023, ("luglio",150))),
                      (("Morbegno","Sondrio"),(2023, ("luglio",165)))
                      )


def media_globale(tupla_pluviometrica):
    c=0
    for posizione,anno,dati in tupla_pluviometrica:
        for (mese,valore) in dati:
            if valore!="N/D" :
                somma=sum(valore)
                c+=1
    media_totale=somma/c
    print("La media totale è: ",media_totale)

def media(tupla_pluviometrica,provincia,mese):
    c=0
    for (paese,provincia),anno,dati in tupla_pluviometrica:
        if nuovo_paese==paese and nuova_provincia==nuova_provincia:
            for (mese,valore) in dati:
                if valore!="N/D" :
                    somma=sum(valore)
                    c+=1
    media_posizione=somma/c
    print("La media totale è: ",media_posizione)    

def pioggiaMax(provincia):
        ValMax=0
        for (paese,provincia),anno,dati in tupla_pluviometrica:
            for (mese,valore) in dati:
                ValMax=max(valore)
                meseMax=mese
            print((meseMax,ValMax))


def pioggiaMin(provincia):
        ValMax=0
        for (paese,provincia),anno,dati in tupla_pluviometrica:
            for (mese,valore) in dati:
                ValMin=min(valore)
                meseMin=mese
            print((meseMin,ValMin))



scelta=input(int("1. Media Globale | 2. Media per provincia e paese | 3.Massimo di pioggia per provincia | 4.Minimo di pioggia per provincia"))

while scelta>0 and scelta <5:
    if(scelta==1):
        media_globale(tupla_pluviometrica) 
        
    elif(scelta==2):
        nuova_provincia=input("inserisci una provincia da analizzare: ")
        nuovo_paese=input("inserisci un paese da analizzare: ")
        media(tupla_pluviometrica,nuova_provincia,nuovo_paese)
            
    elif (scelta==3):
        pioggiaMax("Milano")
        
    elif (scelta==4) :
        pioggiaMin("Milano")

    else:
        print("Scelta errata")