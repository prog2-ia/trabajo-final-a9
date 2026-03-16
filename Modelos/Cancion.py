class Cancion:
    def __init__(self, cancion, duracion, genero, artista, featuring, idioma, gentilicio):
        self._cancion = cancion
        self._duracion = duracion
        self._genero = genero
        self._artista = artista
        self._featuring = featuring
        self._idioma = idioma
        self._gentilicio = gentilicio
    # Usamos _ al principio porque no debe tocarse fuera del código de la biblioteca pero debe ser accesible para otras clases como género

    def __str__(self):
        return f'Nombre: {self._cancion} - Duracion: {self._duracion} min - Genero: {self._genero} - Artista: {self._artista} - Featuring: {self._featuring} - Idioma: {self._idioma}'

    def __repr__(self):
        return f'<Cancion: {self._cancion} | {self._artista} | {self._duracion} min>'

    # Getters actualizados a semi-privados para mayor seguridad
    def get_titulo(self):
        return self._cancion

    def get_duracion(self):
        return self._duracion

    def get_genero(self):
        return self._genero

    def __hash__(self): # Permite set de varias canciones del mismo título
        return hash(self._cancion)

    def __eq__(self, otra_cancion): # Permite eliminar duplicados del mismo título
        if isinstance(otra_cancion, Cancion):
            return self._cancion == otra_cancion.get_titulo()
        return False

    @staticmethod
    def comprobar_existe_duracion(duracion):
        if duracion > 0:
            return True
        return False

    def clasificacion_duracion(self): # Función para clasificar una canción según duración
        if self._duracion < 3:
            return 'Corta'
        elif 3 <= self._duracion < 5:
            return 'Media'
        else:
            return 'Larga'

    def es_colaboracion(self): #Función para comprobar si la canción es una colaboración
        # Si featuring no es None, es una colaboración
        return bool(self._featuring)




