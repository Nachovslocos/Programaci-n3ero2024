Animales=("Conejo","Gato","Perro")
buscar=input("Ingrese el Animal que desea buscar dentro de la lista: ")
if buscar in Animales:
    print("El Animal",buscar,"Si se encuentra en la tupla")
else:
    print("El Animal",buscar,"No se encuentra en la tupla")
