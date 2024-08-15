Ladosfigura=int(input("Ingrese cantidad de lados: "))
if Ladosfigura==4:
    L1=int(input("Ingrese el valor del primer lado: "))
    L2=int(input("Ingrese el valor del segundo lado: "))
    L3=int(input("Ingrese el valor del tercer lado: "))
    L4=int(input("Ingrese el valor del cuarto lado: "))
    
    if L1==L2 and L1==L3 and L1==L4:
        print("Es un cuadrado o un rombo")
elif Ladosfigura==3:
    print("La figura es un triangulo")
