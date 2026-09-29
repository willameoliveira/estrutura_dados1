import unittest
from lista import Lista

class TesteLista(unittest.TestCase):

    def teste_obter(self):
        lista1 = Lista(3)
        lista1.adicionar(2)
        lista1.adicionar(5)
        lista1.adicionar(7)

        self.assertEqual(lista1.obter(0), 2)        

    def teste_obter_fora_fim(self):
        lista1 = Lista(3)
        lista1.adicionar(2)
        lista1.adicionar(5)
        lista1.adicionar(7)

        self.assertEqual(lista1.obter(3), None)         

    def teste_obter_fora_inicio(self):
        lista1 = Lista(3)
        lista1.adicionar(2)
        lista1.adicionar(5)
        lista1.adicionar(7)

        self.assertEqual(lista1.obter(-1), None)         

    def teste_inserir_inicio(self):
        lista1 = Lista(3)
        lista1.adicionar(2)
        lista1.adicionar(5)

        self.assertTrue(lista1.inserir(posicao=0, numero=7))
        self.assertListEqual([7, 2, 5], lista1.array)
    
    def teste_inserir_fim(self):
        lista1 = Lista(3)
        lista1.adicionar(2)
        lista1.adicionar(5)

        self.assertTrue(lista1.inserir(posicao=2, numero=7))
        self.assertListEqual([2, 5, 7], lista1.array)

    def teste_inserir_meio(self):
        lista1 = Lista(3)
        lista1.adicionar(2)
        lista1.adicionar(5)

        self.assertTrue(lista1.inserir(posicao=1, numero=7))
        self.assertListEqual([2, 7, 5], lista1.array)

    def teste_inserir_sem_espaco(self):
        lista1 = Lista(3)
        lista1.adicionar(2)
        lista1.adicionar(5)
        lista1.adicionar(10)

        self.assertFalse(lista1.inserir(posicao=2, numero=7))
        self.assertListEqual([2, 5, 10], lista1.array)

    def teste_inserir_fora_inicio(self):
        lista1 = Lista(3)
        lista1.adicionar(2)
        lista1.adicionar(5)

        self.assertFalse(lista1.inserir(posicao=-1, numero=7))
        self.assertListEqual([2, 5, None], lista1.array)

    def teste_inserir_fora_fim(self):
            lista1 = Lista(3)
            lista1.adicionar(2)
            lista1.adicionar(5)
    
            self.assertFalse(lista1.inserir(posicao=3, numero=7))
            self.assertListEqual([2, 5, None], lista1.array)

    def teste_remover_inicio(self):
        lista1 = Lista(3)
        lista1.adicionar(2)
        lista1.adicionar(5)
        lista1.adicionar(7)

        self.assertTrue(lista1.remover(0))
        self.assertListEqual(lista1.array, [5, 7, None]) 

    def teste_remover_fim(self):
        lista1 = Lista(3)

        lista1.adicionar(2)
        lista1.adicionar(5)
        lista1.adicionar(7)

        self.assertTrue(lista1.remover(2))
        self.assertListEqual(lista1.array, [2, 5, None]) 

    def teste_remover_meio(self):
        lista1 = Lista(3)
        
        lista1.adicionar(2)
        lista1.adicionar(5)
        lista1.adicionar(7)

        self.assertTrue(lista1.remover(1))
        self.assertListEqual(lista1.array, [2, 7, None])

    def teste_remover_numero(self):
        lista1 = Lista(3)
        
        lista1.adicionar(2)
        lista1.adicionar(5)
        lista1.adicionar(7)

        self.assertTrue(lista1.remover_numero(2))
        self.assertListEqual(lista1.array, [5, 7, None])

    def teste_remover_numero_inexistente(self):
        lista1 = Lista(3)
        
        lista1.adicionar(2)
        lista1.adicionar(5)
        lista1.adicionar(7)

        self.assertFalse(lista1.remover_numero(10))
        self.assertListEqual(lista1.array, [2, 5, 7])

if __name__ == '__main__':
    unittest.main()