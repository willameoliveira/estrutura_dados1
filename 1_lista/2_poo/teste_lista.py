import unittest
from lista import Lista

class TesteLista(unittest.TestCase):

    def teste_obter(self):
        lista = Lista(4)
        lista.adicionar(3)
        lista.adicionar(6)
        lista.adicionar(10)

        self.assertEqual(lista.obter(posicao=2), 10)

    def teste_obter_fora_fim(self):
        lista = Lista(4)
        lista.adicionar(3)
        lista.adicionar(6)
        lista.adicionar(10)

        self.assertEqual(lista.obter(posicao=3), None)

    def teste_obter_fora_inicio(self):
        lista = Lista(4)
        lista.adicionar(3)
        lista.adicionar(6)
        lista.adicionar(10)

        self.assertEqual(lista.obter(posicao=-1), None)

if __name__ == '__main__':
    unittest.main()