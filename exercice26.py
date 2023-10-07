nombre=int(input("Donner un nombre SVP : "))

while nombre<=0 :
    nombre=int(input("Donner un nombre SVP (positif non null): "))

somme=0

for i in range(1,nombre* 2,2):
    somme=somme+(i**2)
    

print("le resultat est : ",somme)