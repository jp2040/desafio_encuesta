class Pregunta:
    def __init__(self, enunciado, ayuda=None, requerida=False, alternativas=None):
        """
        Constructor de la clase Pregunta.

        Parameters:
        - enunciado (str): Enunciado de la pregunta (texto).
        - ayuda (str, opcional): Ayuda para la pregunta (opcional).
        - requerida (bool, opcional): Indica si la pregunta es requerida (opcional, por defecto False).
        - alternativas (list, opcional): Lista de Alternativa asociadas a la pregunta (opcional).

        """
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = alternativas if alternativas else []

    def mostrar_pregunta(self):
        """
        Muestra el enunciado, ayuda, y alternativas de la pregunta.

        Returns:
        - str: Cadena que representa la pregunta.

        """
        output = f"Enunciado: {self.enunciado}\nAyuda: {self.ayuda}\nRequerida: {self.requerida}\n"
        for alternativa in self.alternativas:
            output += alternativa.mostrar_alternativa() + "\n"
        return output
