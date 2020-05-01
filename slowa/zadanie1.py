#Zadanie1
zadanie1 = 0
plik = open('tekst.txt')
#with open('tekst.txt') as plik:
for linia in plik:
    for slowo in linia.strip().split():
        znak=slowo[0]
        for litera in slowo[1:]:
          if(znak==litera):
            zadanie1+=1
            break
          else:
            znak=litera
print("Zadanie1",zadanie1)
