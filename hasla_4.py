hasla=open('hasla.txt')
ileHasel=0
cyfry='1234567890'
male='qwertyuiopasdfghjklzxcvbnm'
for haslo in hasla:
    haslo=haslo.strip()
    czyCyfry, czyMale, czyDuze= False, False, False
    for znak in haslo:
        if znak in cyfry:
            czyCyfry = True
            break
    for znak in haslo:
        if znak in male:
            czyMale = True
            break
    for znak in haslo:
        if znak>='A' and znak<='Z': 
            czyDuze = True
            break
    if czyCyfry and czyMale and czyDuze:
        ileHasel+=1
print(ileHasel)
