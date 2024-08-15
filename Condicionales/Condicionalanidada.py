n=int(input("Ingrese un numero: "))
if n==100:
    print("es igual a 100")
elif n<100 and n>9:
     print(n," es una decena")
elif n<10:
    print(n," es una unidad")
elif n<1000 and n>99:
    print(n," es una centena")
elif n>999 and n<100000:
    print(n," es una milesima")
      