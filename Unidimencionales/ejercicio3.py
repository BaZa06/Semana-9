#Promedio de calificaciones 

calificaciones = []
suma = 0
promedio = 0

while True:
    usuario = input("Ingrese una calificación (escriba 'fin' para terminar): ")
    if usuario.lower() == 'fin':
        print("Ingrese 8 calificaciones")
        continue
    try:
        calificacion = float(usuario)
        calificaciones.append(calificacion)
        suma += calificacion
        promedio = suma / len(calificacion)
    except ValueError:
        print("Se producio un error, por favor vuelva a ingresar la calificación: ")
        
print("Las calificaciones ingresadas son: ", calificaciones)
print("El promedio de las calificaciones es: ", promedio)

        