import random

#0
print("Tanulok generálása")

vezNevek=["Ádám", "Balogh", "Lakatos", "Rézműves", "Váradi"]
ferfiKNevek=["Dániel", "Antal", "István", "János", "László", "Péter"]
noiKNevek=["Marianna", "Júlia", "Ildikó", "Bianka", "Mária"]

db=int(input("Kérem a tanulók számát: "))

tanulok=[]
for i in range(db):
    #tanuló neve,ami függ a nemétől
    neme=random.randint(1, 2)
    if neme==1:
    teljesNev = random.choice(vezNevek) + " " + random.choice(ferfiKNevek)
else:
    teljesNev = random.choice(vezNevek) + " " + random.choice(noiKNevek)
#tanuló születési ideje
ev=random.randint(2000, 2005)
honap=random.randint(1, 12)
nap=random.randint(1,28) #mert február mindig tartalmaz 28-át
datum=f"{ev}.{honap:0>2d}.{nap:0>2d}"
#tanuló magassága
magassag=random.randint(150,190)

tanulo =(teljesNev, datum, magassag)

tanulok.append(tanulo)

#2


#3
for item in tanulok:
    print(item)