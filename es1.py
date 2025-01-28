tupla_partite = (
    ("GiocatoreA", "GiocatoreB", 3, 2),
    ("GiocatoreC", "GiocatoreD", 2, 3),
    ("GiocatoreB", "GiocatoreC", 3, 0),
    ("GiocatoreA", "GiocatoreD", 3, 1),
    ("GiocatoreB", "GiocatoreD", 2, 3),
)
def media_set_partita(tupla_partite):
  somma=0
  conta=0
  for dati in tupla_partite:
    giocatore1,giocatore2,setVinti1,setVinti2=dati
    somma+=(setVinti1+setVinti2)
    conta+=2
  if(conta>0):
    media=somma/conta
    print(round(media,2))
  else:
    print("errore nel calcolo della media")    

def media_set_giocatore(tupla_partite, giocatore):
  somma=0
  conta=0
  for dati in tupla_partite:
    giocatore1,giocatore2,setVinti1,setVinti2=dati
    if(giocatore==giocatore1):
        somma+=setVinti1
        conta+=2
    elif(giocatore==giocatore2):
        somma+=setVinti2
        conta+=2
  if(conta>0):
    media=somma/conta
    print(round(media,2))
  else:
    print("errore nel calcolo della media") 

def match_piu_combattuto(tupla_partite):
  max_combattuto=0
  match_combattuto=()
  for dati in tupla_partite:
    giocatore1,giocatore2,setVinti1,setVinti2=dati
    if(setVinti1+setVinti2>max_combattuto):
      max_combattuto=setVinti1+setVinti2
      match_combattuto=(giocatore1,giocatore2,setVinti1,setVinti2)
      print(match_combattuto)
      if(max_combattuto==0):
        print("errore nel calcolo del match piu combattuto")

def match_meno_combattuto(tupla_partite): 
  min_combattuto=10
  match_combattuto=()
  for dati in tupla_partite:
    giocatore1,giocatore2,setVinti1,setVinti2=dati
    if(setVinti1+setVinti2<min_combattuto):
      min_combattuto=setVinti1+setVinti2
      match_combattuto=(giocatore1,giocatore2,setVinti1,setVinti2)
      print(match_combattuto)
      if(min_combattuto==0):
        print("errore nel calcolo del match piu combattuto") 

def percentuale_vittorie_giocatore(tupla_partite, giocatore):
  somma=0
  sommaTotale=0
  for dati in tupla_partite:
    giocatore1,giocatore2,setVinti1,setVinti2=dati
    if(giocatore==giocatore1):
        sommaTotale+=setVinti1+setVinti2
        somma+=setVinti1
        
    elif(giocatore==giocatore2):
        sommaTotale+=setVinti1+setVinti2
        somma+=setVinti2    
  percentuale=(somma/sommaTotale)*100
  print(giocatore,"ha una percentuale di vincita dell: ",percentuale)

  
while(True):
  print("1: media_set_partita")
  print("2: media_set_partita")
  print("3: media_set_partita ")
  print("4: media_set_partita ")
  print("5: media_set_partita")
  print("inserisci 0 per terminare")
  scelta=input("Fai una scelta da 0 a 5")
  if(scelta==1):
    media_set_partita(tupla_partite)
  elif(scelta==2):
    giocatore=input("inserisci il giocatore scelto: ")
    media_set_giocatore(tupla_partite, giocatore)
  elif(scelta==3):
    match_piu_combattuto(tupla_partite)
  elif(scelta==4):
    match_meno_combattuto(tupla_partite)
  elif(scelta==5):
    giocatore=input("inserisci il giocatore scelto: ")
    percentuale_vittorie_giocatore(tupla_partite, giocatore)
  elif(scelta==0):
    break  
  