váltandó = input("Milyen mértékegységben adod meg:")
szám = float(input("Írd be az árváltandó számot:"))
if váltandó=="MB":
    print(f"Az eredmény: {szám/1024}GB")
if váltandó=="GB":
    print(f"Az eredmény: {szám*1024}MB")