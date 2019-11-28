punkty=[]
a = b = 200
promienie=[] #promienie dla poszczególnych punktów
liczbaP = 0 #liczba punktów w kole z zadania 4.1
with open('punkty.txt') as plik:
    for linia in plik:
        punkty.append(linia.strip().split())
        x = int(punkty[-1][0])
        y = int(punkty[-1][1])
        r2 = pow(x-a, 2)+pow(y-b, 2) #odl. od śr koła punktu
        if r2 == 40000:
            print(x, y)
        if r2 < 40000:
            liczbaP+=1
        promienie.append(r2)
            
print("Liczba punktów w kole =", liczbaP)
#koniec zadania 4.1
liczbaP = 0
for i in range(100):
    if promienie[i] <=40000:
        liczbaP+=1
print("%.4f" % (4*liczbaP/100))
