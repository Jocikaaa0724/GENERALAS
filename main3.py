import random

#0
print("Véletlen név generálása")

#1
vezNevek=["Ádám", "Balogh", "Lakatos", "Rézműves", "Váradi"]
ferfiKNevek=["Dániel", "Antal", "István", "János", "László", "Péter"]
noiKNevek=["Marianna", "Júlia", "Ildikó", "Bianka", "Mária"]

neme=input("Kérem megadni a nemet (férfi/nő): ")

#2
if neme.lower()=="férfi":
    teljesNev = random.choice(vezNevek) + " " + random.choice(ferfiKNevek)
elif neme.lower()=="nő":
    teljesNev = random.choice(vezNevek) + " " + random.choice(noiKNevek)
else:
    print("HIBA: rosszul adta meg az ember nemét!!!")
    exit()

    #3
    print(teljesNev)

    