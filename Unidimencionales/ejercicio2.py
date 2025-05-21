#Sumar los elementos de una lista

numeros = []
suma = 0

while True:
    usuario = input("Ingrese un número (escriba ´fin´ para terminar):")
    if usuario.lower() == 'fin':
        break
    try:
        numero = float(usuario)
        numeros.append(numero)
        suma += numero
    except ValueError:
        print("Hubo un error, por favor ingrese un número")
        
print("Los números integrados a la lista son:", numeros)
print("La suma de los números en la lista es:", suma)
    