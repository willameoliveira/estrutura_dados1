"""
Fazendo o array de tamanho 3 guardar um número a mais.
Implementando a partir da cópia para um novo array maior.
"""

capacidade = 3
lista = [None] * capacidade  # Similar a escrever lista = [None, None, None]

lista[0] = 1
lista[1] = 2
lista[2] = 3

print("LISTA ATUAL")
for i in range(3):
    print(lista[i])

nova_lista = [None] * 4

for i in range(3):
    nova_lista[i] = lista[i]

nova_lista[3] = 4
del lista  #  Solicitando que o python apague a lista antiga da memória

print("NOVA LISTA")
for i in range(4):
    print(nova_lista[i])