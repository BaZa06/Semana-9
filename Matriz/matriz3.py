#Matriz nombres
matriz = [["Blanca", "Alejandra", "Ashley"], ["Javier", "Paulo", "Anaixid"], ["Emilio", "Carlos","Genesis"]]
print("-"*32)
for fila in matriz:
    for columna in fila:
        print(f"|| {columna:>6}", end=" |")
    print("| ")
    print("-"*32)

