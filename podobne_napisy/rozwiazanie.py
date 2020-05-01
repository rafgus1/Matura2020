#Zadanie1
plik=open('napisy.txt')
ilewierszy = 0
for linia in plik:
  napisy=linia.strip().split()
  if len(napisy[0])>=3*len(napisy[1]) or len(napisy[1])>=3*len(napisy[0]):
    ilewierszy+=1
print(ilewierszy)


#Zadanie2
plik=open('napisy.txt')
for linia in plik:
  napisy=linia.strip().split()
  if len(napisy[0])>1:
    if napisy[0] in napisy[1]:
      print(napisy, napisy[1][len(napisy[0]):])

#Zadanie3
plik=open('napisy.txt')
wiersze=[]
maks=0
for linia in plik:
  napisy=linia.strip().split()
  napis0=napisy[0][::-1]
  napis1=napisy[1][::-1]
  dl = 0
  for i in range(0, len(napis0)):
    if napis0[i]==napis1[i]:
      dl+=1
    else:
      if dl==maks:
        wiersze.append(napisy)
      if dl>maks:
        maks=dl
        wiersze=[]
        wiersze.append(napisy)
      break
print(maks)
for linia in wiersze:
  print(linia[0], linia[1])
