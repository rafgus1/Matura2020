#Zadanie2
plik = open('tekst.txt')
alfabet="ABCDEFGHIJKALMNOPQRSTUWVXYZ"
sumaz=0
zadanie2 = {}
for znak in alfabet:
  zadanie2[znak]=0
for linia in plik:
  for slowo in linia.strip().split():
    for litera in slowo:
      sumaz+=1
      zadanie2[litera]+=1
for znak in alfabet:
  print(znak,":",zadanie2[znak],round(zadanie2[znak]*100/sumaz,2),"%")
