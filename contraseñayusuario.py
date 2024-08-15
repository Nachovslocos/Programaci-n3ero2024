usuario="Nacho"
contraseña="nachovslocos"
usu=input("Ingrese su usuario: ")
cont=input("Ingrese su contraseña: ")
contador=1
while usu!=usuario or cont!=contraseña and contador<3:
    print ("vuelta numero",contador)
    usu=input("Ingrese su usuario de nuevo: ")
    cont=input("Ingrese su contraseña de nuevo: ")
    contador=contador+1

if usu==usuario and cont==contraseña:
   print ("Bienvenido al sistema :) ")
else:
    print ("No quedan más vueltas para ingresar al sistema")