from lista import Lista

lista1 = Lista(3)

if lista1.adicionar(3):
    print(f"Número 3 adicionado na lista com sucesso!")
else:
    print(f"Número 3 não adicionado. A lista encheu!")

lista1.adicionar(5)
lista1.adicionar(10)

print(f"Pesquisando 10: {lista1.pesquisar(10)}")
print(f"Pesquisando 1: {lista1.pesquisar(1)}")

print("Lista: ")
print(lista1.array)