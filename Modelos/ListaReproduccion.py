class ListaReproduccion:
    def __init__(self, nombre):
        self._nombre = nombre
        self._canciones = []  # Guardaremos los objetos tipo Cancion

    @property
    def nombre(self):
        return self._nombre

    def anyadir_cancion(self, cancion):
        self._canciones.append(cancion)

    def __add__(self, otra_lista):
        nueva = ListaReproduccion(f"{self._nombre} + {otra_lista.nombre}")
        nueva._canciones = self._canciones + otra_lista._canciones
        return nueva

    def __len__(self): #Función para saber cuantas canciones hay en la playlist
        return len(self._canciones)

    def __str__(self):
        return f"Playlist: {self._nombre} [{len(self)} canciones]"