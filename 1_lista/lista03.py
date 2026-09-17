"""
Crie uma lista de capacidade 3 usando array.
Crie um algoritmo que recebe números inteiros em loop e adiciona cada um nessa lista até ela encher. 
Quando a lista encher, imprima uma mensagem dizendo que a lista encheu e pare o programa.
"""

capacidade = 3
lista = [None] * capacidade
tamanho = 0

print("\nADICIONA ATÉ ENCHER\n")
while True:
    num = int(input("Número para adicionar na lista: "))
    if tamanho < capacidade:
            lista[tamanho] = num
            print("Salvo na lista com sucesso!\n")
            tamanho += 1
    else:
          print(f"Número {num} não adicionado! A lista encheu!\n")
          break