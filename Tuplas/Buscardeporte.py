Deportes=("Futbol","Voley","Basquet")
buscar=input("Ingreese el elemento que desea buscar dentro de la lista: ")
if buscar in Deportes:
    print("El elemento",buscar,"Se encuentra dentro de la tupla")
else:
    print("El elemento",buscar,"No se encuentra dentro de la lista")