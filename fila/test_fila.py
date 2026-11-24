from fila import Fila
import pytest

@pytest.fixture
def fila():
    fila = Fila()
    fila.enfileirar(10)
    fila.enfileirar(20)
    fila.enfileirar(30)
    fila.enfileirar(40)
    return fila

def test_desenfileirar(fila):
    assert fila.desenfileirar() == 10
    assert fila.desenfileirar() == 20
    assert fila.desenfileirar() == 30
    assert fila.desenfileirar() == 40
    assert fila.desenfileirar() is None  # Fila vazia

def test_esta_vazia(fila):
    assert not fila.vazia()
    fila.desenfileirar()
    fila.desenfileirar()
    fila.desenfileirar()
    fila.desenfileirar()
    assert fila.vazia()

def test_tamanho(fila):
    assert fila.tamanho() == 4
    fila.desenfileirar()
    assert fila.tamanho() == 3
    fila.desenfileirar()
    fila.desenfileirar()
    fila.desenfileirar()
    assert fila.tamanho() == 0

if __name__ == "__main__":
    pytest.main(["fila/test_fila.py", "-v"])