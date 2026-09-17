"""
Simulando uso de array no Python. Não use os métodos append, pop, etc da lista.
"""

capacidade = 3
lista = [None] * capacidade  # Similar a escrever lista = [None, None, None]
print(lista)

lista[0] = 1
lista[1] = 2
lista[2] = 3

for i in range(3):
    print(lista[i])
