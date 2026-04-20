from Cancion import Cancion

class Album:
    def __init__(self, titulo, anyo, artista):
        self._titulo = titulo
        self._anyo = anyo
        self._artista = artista  # Esperamos recibir un objeto de tipo Artista
        self._canciones = []     # Lista para guardar los objetos Cancion del álbum

    @property # Usamos property para acceder al título de forma segura
    def titulo(self):
        return self._titulo

    def anyadir_cancion(self, cancion):
        # Usamos isinstance para asegurarnos de que solo se añadan Canciones
        if isinstance(cancion, Cancion):
            self._canciones.append(cancion)
        else:
            print("Error: Solo se pueden añadir objetos de tipo Cancion al álbum.")

    def get_duracion_total(self):
        # Recorremos todas las canciones y sumamos su duración
        duracion_total = 0
        for cancion in self._canciones:
            duracion_total += cancion.get_duracion()
        return duracion_total

    def __str__(self):
        return f"Álbum: {self._titulo} ({self._anyo}) - Artista: {self._artista.artista} - {len(self._canciones)} pistas"

    def __repr__(self):
        return f"<Album: {self._titulo} | {self._anyo}>"