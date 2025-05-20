pénz = float(input("Írd be hogy mennyi pénzed van:"))
while pénz>0:
    költés= float(input("Mennyit szeretnél költeni belőle:"))
    if pénz-költés>=0:
        pénz-=költés
        print(f"Ennyi pénzed maradt:{pénz}")
    else:
        print("Ennyit nem költhetsz, nincs ennyi pénzed!")