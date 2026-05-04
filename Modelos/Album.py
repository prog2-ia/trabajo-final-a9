class Album:
    def __init__(self, titulo, anyo, artista):
        self._titulo = titulo
        self._anyo = anyo
        self._artista = artista  # Pasamos el nombre del artista
        self._canciones = []  # Creamos una lista que guarde las canciones

    # Definimos los getter de titulo, anyo y artista
    @property
    def titulo(self):
        return self._titulo

    @property
    def anyo(self):
        return self._anyo

    @property
    def artista(self):
        return self._artista

    @property
    def canciones(self):
        return self._canciones

# Empezamos a definir los métodos
    def anyadir_cancion(self, cancion):
        # Añade un objeto Cancion a la lista interna del álbum
        self._canciones.append(cancion)
        print(f"Se ha añadido '{cancion.titulo}' al álbum '{self._titulo}'.")

    def calcular_duracion_total(self):
        # Suma la duración de todas las canciones del álbum y la devuelve
        duracion_total = 0
        for cancion in self._canciones:
            # Usamos la propiedad de duración
            duracion_total += cancion.duracion
        return duracion_total

    def __str__(self):
        return f"Álbum: '{self._titulo}' ({self._anyo}) - Artista: {self._artista} | {len(self._canciones)} pistas | Duración: {self.calcular_duracion_total()} min"

    def __repr__(self):
        return f"<Album: {self._titulo} | {self._anyo}>"