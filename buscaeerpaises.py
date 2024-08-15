provincias={"buenos aires":"la plata","cordoba":"cordoba","rio negro":"viedma","corrientes":"ciudad de corrientes","entre rios":"parana","tierra del fuego":"ushuaia","misiones":"posadas,","chubut":"rawson","chaco":"resistencia","la pampa":"santa rosa","formosa":"formosa","santa cruz":"rio gallegos","salta":"salta","tucuman":"san miguel de tucuman","mendoza":"mendoza","jujuy":"jujuy","santiago del estero":"santiago del estero","neuquen":"neuquen","san luis":"san luis","la rioja":"la rioja",}
Buscarcapital=input("Ingrese la provicia de la cual desea saber su capital: ")
x=provincias[Buscarcapital]
print("su cappital es: ",x)
print ("_____________________________")

provinciaagregar=input("Ingrese la provincia que desea agregar: ")
Capitalagregar=input("Ingrese la capital de la provincia ")
provincias[provinciaagregar]=Capitalagregar

print("___________________")

for c,v in provincias.items():
   print(c,":",v )

