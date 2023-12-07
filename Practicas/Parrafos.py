class ContadorDePalabras:
    def __init__(self, texto):
        self.texto = texto
        self.conteo_palabras = self._procesar_texto()

    def _limpiar_texto(self):
        # Converte el texto a minúsculas y reemplazar signos de puntuación por espacios
        texto_limpio = self.texto.lower().translate(str.maketrans(",.!?;", "     "))  
        return texto_limpio

    def _procesar_texto(self):
        # Divide el texto en palabras y las cuenta
        texto_limpio = self._limpiar_texto()
        palabras = texto_limpio.split()

        conteo = {}
        for palabra in palabras:
            conteo[palabra] = conteo.get(palabra, 0) + 1
        return conteo

    def obtener_conteo(self):
        # Devuelve el conteo de palabras
        return self.conteo_palabras


class Aplicacion:
    @staticmethod
    def iniciar():
        # Leer la entrada del usuario
        texto_usuario = input("Introduce un párrafo: ")
        contador = ContadorDePalabras(texto_usuario)
        conteo = contador.obtener_conteo()
         # Mostrar el conteo de cada palabra
        for palabra, cantidad in conteo.items():
            print(f"La palabra '{palabra}' aparece {cantidad} {'veces' if cantidad > 1 else 'vez'}.")


# Iniciar la aplicación
Aplicacion.iniciar()
