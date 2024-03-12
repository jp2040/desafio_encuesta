class ListadoRespuestas:
    def __init__(self, usuario, respuestas=None):
        """
        Constructor de la clase ListadoRespuestas.

        Parametros:
        - usuario (Usuario): Usuario asociado al listado de respuestas.
        - respuestas (list, opcional): Lista de respuestas del listado (opcional).

        """
        self.usuario = usuario
        self.respuestas = respuestas if respuestas else []
