"""
Tirar dados
"""

import random


def dado():
    res = random.randint(1,6)
    #print(f"el dado cae en el: {res}")
    return res


veces = int(input("cuantas veces lanzamos el dado? "))
if veces < 1:
    print("no tiraste el dado buhhhh")
else:
    caras = [0,0,0,0,0,0]

    for n in range(0,veces):
        caras[dado()-1]+=1

    print(f"cara 1: {(caras[0]*100)/veces}%")
    print(f"cara 2: {(caras[1]*100)/veces}%")
    print(f"cara 3: {(caras[2]*100)/veces}%")
    print(f"cara 4: {(caras[3]*100)/veces}%")
    print(f"cara 5: {(caras[4]*100)/veces}%")
    print(f"cara 6: {(caras[5]*100)/veces}%")
