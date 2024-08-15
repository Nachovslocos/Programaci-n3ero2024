Deportes={"D1":"Futbol","D2":"Voley","D3":"Basquet"}

for c,v in Deportes.items():
    print(c,":",v)
    if "Futbol" in v:
        print ("El deporte futbol existe y tiene clave de",c)