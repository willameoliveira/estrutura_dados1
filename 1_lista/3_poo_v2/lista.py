class Lista:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.array = [None] * capacidade
        self.tamanho = 0

    def adicionar(self, numero):
       """ Adiciona no fim da lista e retorna True caso tenha espaço.
       Se não tiver espaço, retorna False. """
       
       if self.tamanho < self.capacidade:
            self.array[self.tamanho] = numero
            self.tamanho += 1
            return True
       return False

    def pesquisar(self, numero):
        """ Retorna a posição do número procurado na lista.
        Caso o número não seje encontrado, retorna -1. """
        
        for i in range(self.tamanho):
            if self.array[i] == numero:
                return i
        return -1

    def obter(self, posicao):
        """ Retorna o número guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None. """

        if 0 <= posicao < self.tamanho:
            return self.array[posicao]
        
        return None

    def inserir(self, posicao, numero):
        """ Adiciona um número em uma posição da lista
         empurrando os demais números para o fim da lista.
          Se tem espaço na lista, retorna True, se não, False.
          Se a posição não é válida, também retorna False. """
        
        if self.tamanho < self.capacidade and 0 <= posicao <= self.tamanho:
            for i in range(self.tamanho, posicao, -1):
                self.array[i] = self.array[i-1]
            self.array[posicao] = numero
            self.tamanho += 1
            return True
        
        return False
    
    def remover(self, posicao):
        """ Remove um número de uma posição da lista
        e puxa os demais números para deixar o espaço vazio no fim da lista.
        Ao final, retorna True. Caso a posição não exista na lista, retorna False. """

        if 0 <= posicao < self.tamanho:
            for i in range(posicao, self.tamanho - 1):
                self.array[i] = self.array[i+1]
            self.array[self.tamanho - 1] = None
            self.tamanho -= 1
            return True

        return False

    def remover_numero(self, numero):
        """ Remove um número existente na lista e retorna True.
        Caso o número não seja encontrado, retorna False. """

        return self.remover(posicao=self.pesquisar(numero))