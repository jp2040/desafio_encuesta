class Alternativa:
    def __init__(self, contenido, ayuda=None):
        """
        Constructor de la clase Alternativa.

        Parametros:
        - contenido (str): Contenido de la alternativa (texto).
        - ayuda (str, opcional): Ayuda para la alternativa (opcional).

        """
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self):
        """
        Muestra el contenido y la ayuda de la alternativa.

        Returns:
        - str: Cadena que representa la alternativa.

        """
        return f"Contenido: {self.contenido}\nAyuda: {self.ayuda}" if self.ayuda else f"Contenido: {self.contenido}"
