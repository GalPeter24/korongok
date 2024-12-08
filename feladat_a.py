korongok=[]
sor= input('Add meg a korong helyének sorát!')
oszlop= input('Add meg a korong helyének oszlopát!')

while sor != "" :
    korong = sor + "K" + oszlop
    if korong in korongok:
        print("Itt már szerepel korong")
    else: korongok.append(korong)
    sor= input('Add meg a korong helyének sorát!')
    oszlop= input('Add meg a korong helyének oszlopát!')
print(korongok)