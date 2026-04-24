

class Cancion:
    def __init__(self, cancion, duracion, genero, artista, featuring, idioma, gentilicio):
        self._cancion = cancion
        self._duracion = duracion
        self._genero = genero
        self._artista = artista
        self._featuring = featuring
        self._idioma = idioma
        self._gentilicio = gentilicio

    @property
    def titulo(self):
        return self._cancion.strip().upper()

    @property
    def duracion(self):
        return self._duracion

    @property
    def genero(self):
        return self._genero

    @property
    def artista(self):
        return self._artista

    def __str__(self):
        feat = f" (feat. {self._featuring})" if self._featuring else ""
        return f'{self._cancion}{feat} - {self._artista} ({self._duracion} min)'

    def __repr__(self):
        return f'<Cancion: {self.titulo} | {self._artista}>'

    def __hash__(self):
        return hash(self.titulo)

    def __eq__(self, otra_cancion):
        if isinstance(otra_cancion, Cancion):
            return self.titulo == otra_cancion.titulo
        return False

    def clasificacion_duracion(self):
        if self._duracion < 3: return 'Corta'
        elif 3 <= self._duracion < 5: return 'Media'
        return 'Larga'

