class VerificadorDePalabras:
    def __init__(self, palabra):
        #convertir a minusculas
        self.palabra = palabra.lower()

    def es_heterograma(self):
        # Verifica si cada letra es única en la palabra
        letras_vistas = set()
        for letra in self.palabra:
            if letra in letras_vistas:
                return False
            letras_vistas.add(letra)
        return True

    def es_isograma(self):
        # Verifica si alguna letra se repite en la palabra
        conteo_letras = {}
        for letra in self.palabra:
            if letra in conteo_letras:
                conteo_letras[letra] += 1
                if conteo_letras[letra] > 1:
                    return True
            else:
                conteo_letras[letra] = 1
        return False


class Aplicacion:
    @staticmethod
    def iniciar():
        # Obtener la palabra del usuario
        palabra_usuario = input("Introduce una palabra: ")
        verificador = VerificadorDePalabras(palabra_usuario)
        # Verificar y mostrar si es un heterograma o un isograma
        if verificador.es_heterograma():
            print(f"La palabra '{palabra_usuario}' es un Heterograma.")
        elif verificador.es_isograma():
            print(f"La palabra '{palabra_usuario}' es un Isograma.")
        else:
            print(f"La palabra '{palabra_usuario}' no es ni Heterograma ni Isograma.")


# Iniciar la aplicación
Aplicacion.iniciar()
