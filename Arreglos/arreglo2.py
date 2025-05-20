#Arreglos de tipo entero

array_int = [5, 4, 9, 2, 1]
print("Array de enteros:", array_int)

#Ordenar el arreglo de menor a mayor
array_int.sort()
print("Array de enteros ordenado de menor a mayor:", array_int)

#Buscar un elemneto en el arreglo
elemento = 4
if elemento in array_int:
    print("El elemento {elemento} se encuentra e el arreglo")
else:
    print(F"El elemento {elemento} no se encuentra en el arreglo")
    
    #Insertar un elemento en el arreglo
    array_int:append(6)
    print("Array de enteros después de insertar 6:", array_int)
    