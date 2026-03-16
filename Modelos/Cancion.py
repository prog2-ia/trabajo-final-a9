class Cancion:
    def __init__(self, cancion, duracion, genero, artista, featuring, idioma, gentilicio):
        self.__cancion = cancion
        self.__duracion = duracion
        self.__genero = genero
        self.__artista = artista
        self.__featuring = featuring # En caso de no ser featuring, None o dejar vacío
        self.__idioma = idioma
        self.__gentilicio = gentilicio

    def __str__(self):
        return f'Nombre: {self.__cancion} - Duracion: {self.__duracion} min - Genero: {self.__genero} - Artista: {self.__artista} - Featuring: {self.__featuring} - Idioma: {self.__idioma}'

    def __repr__(self):
        return f'<Cancion: {self.__cancion} | {self.__artista} | {self.__duracion} min>'

    def get_titulo(self):
        return self.__cancion

    def get_duracion(self):
        return self.__duracion

    def __hash__(self): # Permite set de dos mismas canciones
        return hash(self.__cancion)

    # Eliminar duplicados en un set con canciones del mismo titulo.
    def __eq__(self, otra_cancion):
        if isinstance(otra_cancion, Cancion):
            return self.__cancion == otra_cancion.get_titulo()
        return False

    @staticmethod
    def comprobar_existe_duracion(duracion):
        if duracion > 0:
            return True
        return False

    def clasificacion_duracion(self): # Función para clasificar una canción según duración
        if self.__duracion < 3:
            return 'Corta'
        elif 3 <= self.__duracion < 5:
            return 'Media'
        else:
            return 'Larga'

    def es_colaboracion(self): #Función para comprobar si la canción es una colaboración
        # Si featuring no es None, es una colaboración
        return bool(self.__featuring)




