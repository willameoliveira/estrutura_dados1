from no import No

class Lista_Ligada:

    def __init__(self):
        self.no_inicial: No = None
        self.tamanho = 0

    def adicionar(self, item):
        """ Adiciona no fim da lista """

        if self.no_inicial:
            self.no_inicial.proximo = No(item)
        else:
            self.no_inicial = No(item)
        self.tamanho += 1

    def exibir(self):
        """ Exibe os itens da lista """

        no_atual = self.no_inicial
        while no_atual:
            print(no_atual.item, end=" -> ")
            no_atual = no_atual.proximo
        print("null")

    def pesquisar(self, item):
        """ Retorna True caso o item procurado exista na lista e
        False, em caso contrário. """

        pass

    def obter(self, posicao):
        """ Retorna o item guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None. """

        pass

    def inserir(self, posicao, item):
         """ Adiciona um número em uma posição da lista
        empurrando os demais números para o fim da lista.
        Se a posição não é válida, retorna False. """
         
         pass

    def remover(self, posicao):
        """ Remove um número de uma posição da lista
        e puxa os demais itens para o início da lista.
        Ao final, retorna True. Caso a posição não exista na lista, retorna False. """

        pass

    def remover_item(self, item):
        """ Remove um item existente na lista e retorna True.
        Caso o item não seja encontrado, retorna False. """

        pass