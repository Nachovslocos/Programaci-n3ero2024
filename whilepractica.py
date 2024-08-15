prod=[]
rta="Si"
while rta=="Si" or rta=="SI"or rta=="si":
    Opcion=input("1. Agregar productos a la lista\n2. Mostrar la lista\n3. Salir\n")
    if Opcion=="1":
        productoagregar=input("Ingrese el producto que desea agregar a la lista: ")
        prod.append (productoagregar)
    elif Opcion=="2":
        print("Los productos en la lista son: ")
        for p in prod:
            print(p,"")
    elif Opcion=="3":
         rta=input("Desea continuar en la lista (si/no)")
    if rta=="No" or rta=="NO" or rta=="no":
         print("Saliendo del sistema")
         break
else:
    print("Numero ingresado no valido")