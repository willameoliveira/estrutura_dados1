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

nova_lista = [None] * 4

for i in range(3):
    nova_lista[i] = lista[i]

nova_lista[3] = 4
del lista
print(nova_lista)

