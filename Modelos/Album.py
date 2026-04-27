class Album:
    def __init__(self, titulo, anyo, artista):
        self._titulo = titulo
        self._anyo = anyo
        self._artista = artista  # Pasamos el nombre del artista
        self._canciones = []  # Creamos una lista que guarde las canciones

    # Definimos los getter de titulo, anyo y artista
    def get_titulo(self):
        return self._titulo

    def get_anyo(self):
        return self._anyo

    def get_artista(self):
        return self._artista

    def anyadir_cancion(self, cancion):
        # Añade un objeto Cancion a la lista interna del álbum
        self._canciones.append(cancion)
        print(f"Se ha añadido '{cancion.get_titulo()}' al álbum '{self._titulo}'.")

    def get_canciones(self):
        return self._canciones

    def calcular_duracion_total(self):
        # Suma la duración de todas las canciones del álbum y la devuelve
        duracion_total = 0
        for cancion in self._canciones:
            # Usamos el getter de duración que ya hemos creado anteriormente en el archivo de Canción
            duracion_total += cancion.get_duracion()
        return duracion_total

    def __str__(self):
        return f"Álbum: '{self._titulo}' ({self._anyo}) - Artista: {self._artista} | {len(self._canciones)} pistas | Duración: {self.calcular_duracion_total()} min"

    def __repr__(self):
        return f"<Album: {self._titulo} | {self._anyo}>"