numerosenteros=[]

while True:
    numero =int(input("Ingrese un numero entero: ")) 
    numerosenteros.append(numero)
    if numero==0:
    
          break
    
    print(numerosenteros)
    print("El numero mayor es: ")
    print(max(numerosenteros))