
from operator import contains


print('Vali millist sa tahad teha:')
print("1 - Aastaaeg")
print("2 - Kiiruse Kontroll")
print("3 - Taksosõit")
valik = int(input('Sinu Valik: '))

if valik == 1:
    print("--------------------------------")
    print("Aastaaeg") # parandasin "'" - """
    kuu=int(input("sisesta kuu number (1-12) => "))
    if kuu<1 and kuu>12:
        print("vigane kuu")
    elif kuu>=12 or kuu<=2: # lisasin ">"
        print("talv")
    elif 3<=kuu<=5:
        print("kevad")
    elif 6<=kuu<=8: #lisasin : ja parantasin syntaxi
        print("suvi") # panin 4 klahvi yles poole, muidu on vale syntax
    else:
        print("sügis")
    print()
elif valik == 2:
    print("--------------------------------")
    print("Kiiruse kontroll")
    lubatud=int(input("Sisesta lubatud kiirus (km/h) => ")) # lisasin sulu ) lõppu
    kiirus=int(input("Sisesta tegelik kiirus (km/h) => ")) # lisasin "int" algusesse
    yletus= (kiirus - lubatud)
    #print(yletus) # debug
    if yletus<=0: # vahetasin järjekorda =< <=
        print("Kiirust ei ületatud")
    elif yletus <= 19: #vahetasin (rohkem kui 0) vähem kui 20
        print("Hoiatus")
    elif yletus>= 19 < 40: #  "elif yletus>20:" checki asemel ma vaatan kas arv on 20 ja 39 vahel
        print("Trahv")
    elif yletus>= 40:
        print("Juhiluba võetakse ära")
    print()
elif valik == 3:
    print("--------------------------------")
    print("Taksosõit")
    km=float(input("Sisesta sõidu pikkus (km) => "))
    oo=input("Kas sõit on öösel (jah/ei)? => ")
    hind=3+km+0.8
    if km < 0:
        print("Negatiivset arvu ei saa sisestada")
    if oo=="jah" or oo=="JAH": #lisasin : lõppu, "and" asemel panin "or"
        if km >= 50: # kas on rohkem kui 50 km soit, kui on siis allahindlus 10%
            hind = hind * 10 / 100
            print("Sõidu hind:", round(hind,2), "€", " (alahindlus 10%)") 
        elif km <= 49:
            hind=hind*1.2
            print("Sõidu hind:", round(hind,2), "€") # lisasin ) lõppu, syntaxit panen 4 klahvi yles poole
elif valik != 1 != 2 != 3:
    print("Vale number 1-3")