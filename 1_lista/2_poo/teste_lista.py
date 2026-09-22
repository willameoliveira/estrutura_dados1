from lista import Lista

lista1 = Lista(3)

print(lista1.capacidade)
print(lista1.tamanho)
print(lista1.array)

if lista1.adicionar(3) == True:
    print(f"Número 3 adicionado na lista com sucesso!")
else:
    print(f"Número 3 não adicionado. A lista encheu!")
    
lista1.adicionar(5)
lista1.adicionar(10)
lista1.adicionar(15)

print("Lista: ")
print(lista1.array)
