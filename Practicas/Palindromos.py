class VerificadorDePalindromo:
    def __init__(self, texto):
        self.texto_original = texto
        self.texto_limpio = self._limpiar_texto() # Preprocesar el texto

    def _limpiar_texto(self):
        # Eliminar espacios y signos de puntuación, y convertir a minúsculas
        return "".join(char.lower() for char in self.texto_original if char.isalnum())

    def es_palindromo(self):
        # Comparar la cadena con su versión invertida
        return self.texto_limpio == self.texto_limpio[::-1]


class Aplicacion:
    @staticmethod
    def iniciar():
        # Obtiene la cadena del usuario y verificar si es un palíndromo
        texto_usuario = input("Introduce una cadena para verificar si es un palíndromo: ")
        verificador = VerificadorDePalindromo(texto_usuario)

        if verificador.es_palindromo():
            print("Es un palíndromo.")
        else:
            print("No es un palíndromo.")


# Iniciar la aplicación
Aplicacion.iniciar()
