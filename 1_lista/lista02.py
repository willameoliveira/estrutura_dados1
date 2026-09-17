"""
Implementando redimensionamento de array a partir da cópia para um novo array maior
"""

capacidade = 3
lista = [None] * capacidade  # Similar a escrever lista = [None, None, None]
print(lista)

lista[0] = 1
lista[1] = 2
lista[2] = 3

for i in range(3):
    print(lista[i])

capacidade = 4
nova_lista = [None] * 4

for i in range(3):
    nova_lista[i] = lista[i]

del lista
print(nova_lista)