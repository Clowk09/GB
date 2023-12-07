from Parrafos import ContadorDePalabras


# flujo feliz
def test_contador_de_palabras_happy_flow():
    texto = "Este es un ejemplo de texto. Contiene varias palabras repetidas, como ejemplo."
    contador = ContadorDePalabras(texto)
    conteo_palabras = contador.obtener_conteo()

    assert conteo_palabras["este"] == 1
    assert conteo_palabras["es"] == 1
    assert conteo_palabras["un"] == 1
    assert conteo_palabras["ejemplo"] == 2
    assert conteo_palabras["de"] == 1
    assert conteo_palabras["texto"] == 1
    assert conteo_palabras["contiene"] == 1
    assert conteo_palabras["varias"] == 1
    assert conteo_palabras["palabras"] == 1
    assert conteo_palabras["repetidas"] == 1
    assert conteo_palabras["como"] == 1

# flujo alternativo
def test_contador_de_palabras_alternating_flow():
    texto = "Este es un ejemplo de texto. Contiene varias palabras repetidas, como ejemplo."
    contador = ContadorDePalabras(texto)
    conteo_palabras = contador.obtener_conteo()

    assert conteo_palabras["este"] == 1
    assert conteo_palabras["es"] == 1
    assert conteo_palabras["un"] == 1
    assert conteo_palabras["ejemplo"] == 2
    assert conteo_palabras["de"] == 1
    assert conteo_palabras["texto"] == 1
    assert conteo_palabras["contiene"] == 1
    assert conteo_palabras["varias"] == 1
    assert conteo_palabras["palabras"] == 1
    assert conteo_palabras["repetidas"] == 1
    assert conteo_palabras["como"] == 1

    # Texto vacío
    texto_vacio = ""
    contador_vacio = ContadorDePalabras(texto_vacio)
    conteo_palabras_vacio = contador_vacio.obtener_conteo()

    assert conteo_palabras_vacio == {}

    # texto con un solo caracter
    texto_puntuacion = ",.!?;"
    contador_puntuacion = ContadorDePalabras(texto_puntuacion)
    conteo_palabras_puntuacion = contador_puntuacion.obtener_conteo()

    assert conteo_palabras_puntuacion == {}