#Matriz letras por nombre
matriz = [["Blanca", "Alejandra", "Ashley"], ["Javier", "Paulo", "Anaixid"], ["Emilio", "Carlos","Genesis"]]
print("-"*40)

for fila in matriz:
    for columna in fila:
        print(f"| {columna:>6}", end=" |")
    print("| ")
    print("-"*40)
    
cantidad_letras = []
    
for fila in matriz:
    new_row = []
    for columna in fila:
        new_row.append(len(columna))
    cantidad_letras.append(new_row)
    
for fila in cantidad_letras:
    for columna in fila:
        print(f"| {columna:>6}", end=" |")
    print("| ")
    print("-"*40)