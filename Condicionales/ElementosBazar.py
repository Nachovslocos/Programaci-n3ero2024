ElemBazar=[]
while ElemBazar==True: #Una condicion que siempre sera verdadera 
    
    opcion=int(input("Menu de opcione\n1-Agregar elementos a la lista-\n2-Eliminar elementos de la lista\n3-Modificar elementos en la lista\n4-Mostrar elementos de la lista\n5-Salir del programa\n"))
    if opcion==1: #La primera opcion nos sirve para poder agregar un prducto a la lista 
        elementoagregar=input("Inrese el nombre del elemento que desea agregar: ")
        ElemBazar.append(elementoagregar) #Se agrega un elemento a la lista
    elif opcion==2: #Esta opcion nos permite eliminar un elemento de la lista 
        elementoAeliminar=input("Ingrese el nombre del elemento que desea eliminar") #El usuario ingresa el nombre del elemeto que desea eliminar
        if elementoAeliminar in ElemBazar: #Se busca el elemento que desea eliminar en la lista 
            ElemBazar.remove(elementoAeliminar) #Se elimina un elemento de la lista usando el "remove"
            print("Elemento eliminado exitosamente") #Muestra al usuario que el elemento fue eliminado 
        else: #Sino se encuentra el elemento en la lista
            print("El elemento que desea eliminar no se encuentra en la lista") #Muestra al usuario una alternativa por si no se encuentra el elemento
    elif opcion==3: #Esta opcion nos permite modificar un elemento 
        elementoAmodificar=input("Ingrese el nombre del elemento que desea odificar: ") #Se le pide al usuario que ingrese el nombre del elemento que desea modificar de la lista 
        if elementoAmodificar in ElemBazar: #Se busca el elemento a modificar en la lista
            elementoModificacion=input("Ingrese el elemento por el que quiere modifica: ") #El usuario ingresa el nombre del elemeneto que va a modificar por el otro
            index = ElemBazar.index(elementoAmodificar) #A base del indice nos ayuda modificar un elemento
            ElemBazar[index] = elementoModificacion
        else:
             print("El elemento a midificar no existe en la lista") #Muestra al usuario si es que existe o no exite el elemento a modificar
    elif opcion==4: #Con esta opcion nos muestra la lista 
        print("Elementos en la lista: \n",ElemBazar) #Muestra un cartel y debajo los elementos de la lista    
    elif opcion==5: #Esta opcion nos sirve para salir del sitema si es que se eligio la opcion 5            
        print("Saliendo del sistema") #Aca de muestra
        break #Nos sirve para cortar el while
    else:
        print("La opción ingresada es invalida")  
    
        
       
        