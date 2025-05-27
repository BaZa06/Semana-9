#Matriz escalar 15%

descuento = float(input("Ingrese el descuento: "))
matriz = [[19, 50], [49, 83]]
matriz_d= []
print("-"*30)

for fila in matriz:
    for columna in fila:
        print(f"| {columna}", end=" ")
    print("|")
    print("-"*30)
    
print("Descuento: ")

for fila in matriz:
    new_row = []
    for columna in fila:
        new_row.append(columna * (1 - descuento))
    matriz_d.append(new_row)
    
for fila in matriz_d:
    for columna in fila:
        print(f"| {columna}", end=" ")
    print("|")
    print("-"*30)
    