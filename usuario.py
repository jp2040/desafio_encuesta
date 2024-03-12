class Usuario:
    def __init__(self, correo, edad, region):
        """
        Constructor de la clase Usuario.

        Parametros:
        - correo (str): Correo del usuario.
        - edad (int): Edad del usuario.
        - region (int): Región del usuario.

        """
        self.correo = correo
        self.edad = edad
        self.region = region

    def responder_encuesta(self, encuesta):
        """
        Permite al usuario responder una encuesta.

        Parametros:
        - encuesta (Encuesta): Encuesta a la que el usuario responderá.

        """
        listado_respuestas = ListadoRespuestas(self)
        encuesta.agregar_listado_respuestas(listado_respuestas)

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
