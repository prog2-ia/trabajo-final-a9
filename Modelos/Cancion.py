# Hacemos que Cancion herede de ABC, impidiendo que se puedan crear objetos 'Cancion' genéricos
# Hacemos que 'Cancion' solo sirve para crear otras clases
from abc import ABC, abstractmethod
class Cancion(ABC):
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

# Definimos el método abstracto
# Cada canción lo va a implementar a su manera por lo que no tiene código
# Garantiza el polimorfismo en las clases hijas
    @abstractmethod
    def reproducir(self):
        """Método abstracto que obliga a las hijas a implementarlo"""
        pass

