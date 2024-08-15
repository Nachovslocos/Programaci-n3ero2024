Bizcochuelo={"Huevos":"4","Harina":"2 tazas","azucar":"2 tazas","polvo para hornear":"1 cucharadita","leche":"1/2 taza","Escencia de vainilla":"1 Chdita",}
buscaringrediente=input("Ingrese el ingrediente que desea buscar: ")
x=Bizcochuelo[buscaringrediente]
print(x)
print ("___________________________")
for c,v in Bizcochuelo.items():
   print(c,":",v )
