Temperatura=float(input("Ingrese la temperatura actual: "))
menuplatosfrios=["Ensalada completa","Ensalada Cenar"]
menuplatoscalienetes=["Polenta","Guiso","Estofado"]
if Temperatura>=25:
    print ("El menu sugerido para este tiempo de calor es: ",menuplatosfrios)
else:
    print ("El menu sugerido para este tiempo de frio es: ",menuplatoscalienetes)