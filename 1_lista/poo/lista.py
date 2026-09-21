class Lista:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.array = [None] * capacidade
        self.tamanho = 0

    def adicionar(self, numero):
        if self.tamanho < self.capacidade:
            self.array[self.tamanho] = numero
            self.tamanho += 1
            print(f"Número {numero} adicionado na lista com sucesso!")
        else:
            print(f"Número {numero} não adicionado. A lista encheu!")