import pytest
from Palindromos import VerificadorDePalindromo

def test_palindromo_happy_flow():
    # caso para palindromo
    texto = "A man, a plan, a canal, Panama!"
    verificador = VerificadorDePalindromo(texto)
    assert verificador.es_palindromo() == True

def test_palindromo_alternating_flow():
    # caso para no palindromo
    texto = "Hello, world!"
    verificador = VerificadorDePalindromo(texto)
    assert verificador.es_palindromo() == False

def test_palindromo_empty_text():
    # caso para texto vacio
    texto = ""
    verificador = VerificadorDePalindromo(texto)
    assert verificador.es_palindromo() == True

def test_palindromo_single_character():
    # caso para un solo caracter
    texto = "a"
    verificador = VerificadorDePalindromo(texto)
    assert verificador.es_palindromo() == True

def test_palindromo_whitespace():
    # caso para espacios en blanco
    texto = "   "
    verificador = VerificadorDePalindromo(texto)
    assert verificador.es_palindromo() == True