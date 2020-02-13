plik = open('dane_obrazki.txt ')
obrazy = []
obraz = []
for linia in plik:
    if len(linia.strip())>0:
        obraz.append(linia.strip())
    else:
        obrazy.append(obraz)
        obraz=[]
#zadanie 1
rewers = 0
for obraz in obrazy:
    ileJedynek=0
    ileZer = 0
    for linia in obraz[0:20]:
        ileJedynek+=linia[0:-1].count('1')
    if ileJedynek>200:
        rewers+=1
print(rewers)
#zadanie 2
rekurencyjne=0
pierwszy = True
for obraz in obrazy:
    c1,c2,c3,c4=[],[],[],[]
    for linia in obraz[0:10]:
        c1.append(linia[0:10])
        c2.append(linia[10:20])
    for linia in obraz[10:20]:
        c3.append(linia[0:10])
        c4.append(linia[10:20])
    if c1==c2==c3==c4:
        rekurencyjne+=1
        if pierwszy:
            for wiersz in obraz[0:20]:
                print(wiersz[0:20])
            pierwszy=False
print(rekurencyjne)
#zadanie3
bledyMax=0
poprawne=0
nienaprawialne=0
naprawialne = 0
numerObrazka = 1
for obraz in obrazy:
    pion=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    wierszeB=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #z4
    kolumnyB=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #z4
    bladW=0
    bladK=0
    poprawneWiersze=True
    poprawneKolumny=True
    numerWiersza=0
    for linia in obraz[0:20]:
        if linia[0:20].count('1')%2==int(linia[-1]):
            pass
        else:
            wierszeB[numerWiersza]=1
            bladW+=1
            poprawneWiersze=False
        for i in range(0,20):
            if linia[i]=='1':
                pion[i]+=1
        numerWiersza+=1
    ostatni=obraz[-1]
    for i in range(0,20):
        if pion[i]%2==int(ostatni[i]):
            pass
        else:
            kolumnyB[i]=1
            bladK+=1
            poprawneKolumny=False
    if poprawneKolumny and poprawneWiersze:
        poprawne+=1
    elif bladW>1 and bladK>1 or bladW>1 or bladK>1:
        nienaprawialne+=1
    else:
        print(numerObrazka)      
        for i in range(0,20):
            if wierszeB[i]:
                print(i+1)
        for i in range(0,20):
            if kolumnyB[i]:
                print(i+1)
                print(" ")
    if bledyMax<bladK+bladW:
        bledyMax=bladK+bladW
    numerObrazka+=1
naprawialne = 200-poprawne-nienaprawialne
print(poprawne, naprawialne, nienaprawialne, bledyMax)

    
