from lista_ligada import ListaLigada
import pytest


@pytest.fixture
def lista():
    lista = ListaLigada()
    lista.inserir_inicio(10)
    lista.inserir_inicio(20)
    lista.inserir_inicio(30)
    lista.inserir_inicio(40)
    return lista


def test_exibir_lista(lista):
    assert str(lista) == "40 -> 30 -> 20 -> 10 -> null"


def test_inserir_inicio(lista):
    lista.inserir_inicio(1)
    assert lista.primeiro.item == 1
    assert str(lista) == "1 -> 40 -> 30 -> 20 -> 10 -> null"


def test_inserir_inicio_lista_vazia():
    lista_vazia = ListaLigada()
    lista_vazia.inserir_inicio(1)
    assert str(lista_vazia) == "1 -> null"


def test_adicionar(lista):
    lista.adicionar(50)
    assert str(lista) == "40 -> 30 -> 20 -> 10 -> 50 -> null"


def test_pesquisar(lista):
    assert lista.pesquisar(20) is True
    assert lista.pesquisar(100) is False


def test_pesquisar_lista_vazia():
    lista_vazia = ListaLigada()
    assert lista_vazia.pesquisar(1) is False


def test_obter(lista):
    assert lista.obter(0) == 40
    assert lista.obter(1) == 30
    assert lista.obter(2) == 20
    assert lista.obter(3) == 10
    assert lista.obter(4) is None


def test_obter_lista_vazia():
    lista_vazia = ListaLigada()
    assert lista_vazia.obter(0) is None
    assert str(lista_vazia) == "null"


def test_inserir(lista):
    assert lista.inserir(0, 1) is True
    assert str(lista) == "1 -> 40 -> 30 -> 20 -> 10 -> null"


def test_inserir_posicao_invalida(lista):
    assert lista.inserir(-1, 1) is False
    assert lista.inserir(5, 1) is False
    assert str(lista) == "40 -> 30 -> 20 -> 10 -> null"


def test_inserir_meio(lista):
    assert lista.inserir(2, 25) is True
    assert str(lista) == "40 -> 30 -> 25 -> 20 -> 10 -> null"


def test_inserir_fim(lista):
    assert lista.inserir(4, 5) is True
    assert str(lista) == "40 -> 30 -> 20 -> 10 -> 5 -> null"


def test_remover_inicio(lista):
    assert lista.remover_inicio() == 40
    assert str(lista) == "30 -> 20 -> 10 -> null"


def test_remover_inicio_lista_vazia():
    lista_vazia = ListaLigada()
    assert lista_vazia.remover_inicio() is None
    assert str(lista_vazia) == "null"


def test_remover_posicao(lista):
    assert lista.remover(2) == 20
    assert str(lista) == "40 -> 30 -> 10 -> null"


def test_remover_posicao_invalida(lista):
    assert lista.remover(-1) is None
    assert lista.remover(4) is None
    assert str(lista) == "40 -> 30 -> 20 -> 10 -> null"


def test_remover_fim(lista):
    assert lista.remover(3) == 10
    assert str(lista) == "40 -> 30 -> 20 -> null"


def test_remover_lista_vazia():
    lista_vazia = ListaLigada()
    assert lista_vazia.remover(0) is None
    assert str(lista_vazia) == "null"


def test_remover_item(lista):
    assert lista.remover_item(30) is True
    assert str(lista) == "40 -> 20 -> 10 -> null"


def test_remover_item_inexistente(lista):
    assert lista.remover_item(100) is False
    assert str(lista) == "40 -> 30 -> 20 -> 10 -> null"


def test_remover_item_lista_vazia():
    lista_vazia = ListaLigada()
    assert lista_vazia.remover_item(1) is False
    assert str(lista_vazia) == "null"


if __name__ == "__main__":
    pytest.main(["lista_ligada/test_lista_ligada.py", "-v"])