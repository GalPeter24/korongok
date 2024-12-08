korongok=[]
sor= input('Add meg a korong helyének sorát!')
while sor != "" :
    sorszam= int(sor)
    if sorszam <= 8 and sorszam > 0:
        oszlop= input('Add meg a korong helyének oszlopát!')
        oszlopszam = int(oszlop)
        if oszlopszam <= 8 and oszlopszam > 0 :
            korong = sor + "K" + oszlop
            if korong in korongok:
                print("Itt már szerepel korong")
            else:korongok.append(korong)
        else: print('hibás oszlopszám') 
    else: print('hibás sorszám')
    sor= input('Add meg a korong helyének sorát!')
print(korongok)