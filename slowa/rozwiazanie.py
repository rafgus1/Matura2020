#Zadanie1
plik=open('tekst.txt')
slowa=[]
ileslow=0
for linia in plik:
  slowa=linia.strip().split()
for slowo in slowa:
  znak0=slowo[0]
  for znak in slowo[1:]:
    if znak0==znak:
      ileslow+=1
      break
    else:
      znak0=znak
print(ileslow)
  
#Zadanie2
alfabet="ABCDEFGHIJKLMNOPQRSTUWVXYZ"
litery={}
ileliter=0
for litera in alfabet:
  litery[litera]=0
for slowo in slowa:
  for znak in slowo:
    litery[znak]+=1
    ileliter+=1
for litera in alfabet:
  ile=litery[litera]
  print(litera,":",ile,"(",round(100*ile/ileliter, 2),"%)")

#Zadanie3
spolgloski="BCDFGHJKLMNPQRSTWVXZ"
maks=0
ileslow=0
tekst=""
for slowo in slowa:
  dl=0
  for znak in slowo:
    if znak in spolgloski:
      dl+=1
    else:
      if dl==maks:
        ileslow+=1
      if dl>maks:
        maks=dl
        ileslow=1
        tekst=slowo
      dl=0
print(maks, ileslow, tekst)
