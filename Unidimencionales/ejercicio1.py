#Cargar una lista manualmente

numeros = []

while True:
    usuario = input("Ingrese un número (a 'fin' para terminar): ")
    if usuario.lower() == 'fin':
        break
    try:
        numero = int(usuario)
        if numero > 0:
            print("El número es entero")
        else:
            print("El número no es entero:")
        numeros.append(numero)
    except ValueError:
        print("Entrada no válida, por favor ingrese un número entero o 'fin'.")

print("Los números ingresados son:", numeros)