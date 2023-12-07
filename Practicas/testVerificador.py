import pytest
from Verificador import VerificadorDePalabras

# flujo feliz
def test_es_heterograma_true():
    verificador = VerificadorDePalabras("abcdefg")
    assert verificador.es_heterograma() == True

def test_es_heterograma_false():
    verificador = VerificadorDePalabras("abbcdefg")
    assert verificador.es_heterograma() == False

def test_es_isograma_true():
    verificador = VerificadorDePalabras("abcdefg")
    assert verificador.es_isograma() == True

def test_es_isograma_false():
    verificador = VerificadorDePalabras("abbcdefg")
    assert verificador.es_isograma() == False

# flujo alternativo
def test_es_heterograma_empty_string():
    verificador = VerificadorDePalabras("")
    assert verificador.es_heterograma() == True

def test_es_isograma_empty_string():
    verificador = VerificadorDePalabras("")
    assert verificador.es_isograma() == False

def test_es_heterograma_single_character():
    verificador = VerificadorDePalabras("a")
    assert verificador.es_heterograma() == True
