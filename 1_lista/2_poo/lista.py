class Lista:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.array = [None] * capacidade
        self.tamanho = 0

    def adicionar(self, numero):
        if self.tamanho < self.capacidade:
            self.array[self.tamanho] = numero
            self.tamanho += 1
            return True
        return False

    def pesquisar(self, numero):
        for i in range(self.tamanho):
            if self.array[i] == numero:
                return i
        return -1

    def obter(self, posicao):
        """ Retorna o número guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None. """
        pass

    def inserir(self, posicao, numero):
        """ Adiciona um número em uma posição da lista
         empurrando os demais números para o fim da lista.
          Se tem espaço na lista, retorna True, se não, False. """
        pass
    
    def remover(self, posicao):
        """ Remove um número de uma posição da lista
        e puxa os demais números para deixar o espaço vazio no fim da lista.
        Ao final, retorna True. Caso a posição não exista na lista, retorna False. """
        pass
    