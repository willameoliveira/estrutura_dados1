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


if __name__ == "__main__":
    pytest.main(["2_lista_ligada/2_listav2/test_lista_ligadav2.py", "-v"])