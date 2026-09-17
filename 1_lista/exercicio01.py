""""
Criar um algoritmo que adiciona números na lista estática (array). 
Quando a lista encher, imprima mensagem dizendo que a lista encheu.
Depois, crie outro algoritmo que pesquisa se determinado número existe na lista.
"""
capacidade = 3
lista = [None] * capacidade
tamanho = 0

print("\nADICIONA ATÉ ENCHER")
while True:
    num = input("Número para adicionar na lista: ")
    if tamanho < capacidade:
            lista[tamanho] = num
            print("Salvo na lista com sucesso!\n")
            tamanho += 1
    else:
          print(f"Número {num} não adicionado! A lista encheu!\n")
          break

print("\nPESQUISA")

num = input("Número a pesquisar (ENTER para encerrar): ")
while num:
    achou = False
    for i in range(tamanho):
          if (lista[i] == num):
                print(f"Número {num} encontrado!")
                achou = True
                break
    if not achou:
          print("Número não encontrado!")
    num = input("\nNúmero a pesquisar (ENTER para encerrar): ")