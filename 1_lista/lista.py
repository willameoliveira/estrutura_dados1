"""
Crie uma lista usando array.
Criar uma função que adiciona número na lista. 
Quando a lista encher, imprima mensagem dizendo que a lista encheu.
Criar uma função que pesquisa se determinado número existe na lista
"""

def adiciona(lista, capacidade, tamanho_atual, numero):
    if tamanho_atual < capacidade:
        lista[tamanho_atual] = numero
        return True
    else:
        return False

def pesquisa(lista, tamanho_atual, numero):
    pass

capacidade = 10
lista = [None] * capacidade
tamanho = 0

for i in range(11):
    num = int(input("Número: "))
    if adiciona(lista, capacidade, tamanho, num):
        print("Salvo na lista com sucesso!")
        tamanho += 1
    else:
        print("A lista encheu!")
    