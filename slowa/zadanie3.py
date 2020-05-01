#Zadanie 3
plik = open('tekst.txt')
spol = "BCDFGHJKLMNPQRSTWVXZ"
maks=0
pierwsze=""
ile=0
index=0
for linia in plik:
  for slowo in linia.strip().split():
    index+=1
    dl=0
    for litera in slowo:
      if litera in spol:
        dl+=1
      else:
        if dl>maks:
          maks=dl
          pierwsze = slowo
          ile=1
        else:
          if dl == maks:
            ile+=1
        dl=0
print(maks,ile,pierwsze)
