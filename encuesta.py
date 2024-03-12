class Encuesta:
    def __init__(self, nombre, preguntas=None, respuestas=None):
        """
        Constructor de la clase Encuesta.

        Parametros:
        - nombre (str): Nombre de la encuesta (texto).
        - preguntas (list, opcional): Lista de Pregunta asociadas a la encuesta (opcional).
        - respuestas (list, opcional): Lista de ListadoRespuestas asociados a la encuesta (opcional).

        """
        self.nombre = nombre
        self.preguntas = preguntas if preguntas else []
        self.respuestas = respuestas if respuestas else []

    def mostrar_encuesta(self):
        """
        Muestra el nombre y las preguntas de la encuesta.

        Returns:
        - str: Cadena que representa la encuesta.

        """
        output = f"Nombre de la Encuesta: {self.nombre}\n"
        for pregunta in self.preguntas:
            output += pregunta.mostrar_pregunta() + "\n"
        return output

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, preguntas=None, respuestas=None, edad_minima=None, edad_maxima=None):
        """
        Constructor de la clase EncuestaLimitadaEdad, una subclase de Encuesta.

        Parametros:
        - edad_minima (int): Edad mínima permitida para la encuesta.
        - edad_maxima (int): Edad máxima permitida para la encuesta.

        """
        super().__init__(nombre, preguntas, respuestas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def agregar_listado_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas solo si la edad del usuario asociado está entre las edades límites.

        Parametros:
        - listado_respuestas (ListadoRespuestas): Listado de respuestas a agregar.

        """
        if self.edad_minima <= listado_respuestas.usuario.edad <= self.edad_maxima:
            self.respuestas.append(listado_respuestas)

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, preguntas=None, respuestas=None, regiones=None):
        """
        Constructor de la clase EncuestaLimitadaRegion, una subclase de Encuesta.

        Parametros:
        - regiones (list): Lista de regiones permitidas para la encuesta.

        """
        super().__init__(nombre, preguntas, respuestas)
        self.regiones = regiones if regiones else []

    def agregar_listado_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas solo si la región del usuario asociado está en la lista de regiones permitidas.

        Parametros:
        - listado_respuestas (ListadoRespuestas): Listado de respuestas a agregar.

        """
        if listado_respuestas.usuario.region in self.regiones:
            self.respuestas.append(listado_respuestas)
