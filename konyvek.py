konyvek = []
with open('konyvek-adatok.txt', "r", encoding="UTF-8") as olvaso:
    olvaso.readline()
    for sor in olvaso:
        konyvek.append(sor.strip().split(";"))

print(f"A listában {len(konyvek)} db könyv található")
műfaj=input("Írj be egy űfajt:")
összoldal=0
db=0
for konyv in konyvek:
    if konyv[1]==műfaj:
        db+=1
        összoldal+=int(konyv[2])
print(f'{db}db könyv tartozik ebbe a műfajba {összoldal}összoldalszámmal')

van=False
for konyv in konyvek:
    if 1600<=konyv[3]<=1699 and konyv[1]=='színmű':
        van=True
if van:
    print("1600 és 1699 között van sziínműbe tartozó mű")
else:
    print("1600 és 1699 között nincs sziínműbe tartozó mű")

def hossz(konyv):
    if int(konyv[2])>600:
        return "hosszú"
    if 200<int(konyv[2])<600:
        return "közép"
    if int(konyv[2])<200:
        return "rövid"
    
with open('negyezer-export.txt', 'w') as iro:
    for konyv in konyvek:
        if int(konyv)==4000:
            olvaso.write(f'{konyv[0]} {hossz(konyv)}')
