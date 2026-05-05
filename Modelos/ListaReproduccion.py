class ListaReproduccion:
    def __init__(self, nombre):
        self._nombre = nombre
        self._canciones = []  # Guardaremos los objetos tipo Cancion

    @property
    def nombre(self):
        return self._nombre

    def anyadir_cancion(self, cancion):
        from .Cancion import Cancion
        if isinstance(cancion, Cancion):
            self._canciones.append(cancion)
        return self

    def __add__(self, otra_lista): #Fusionar 2 listas de reproducción
        nueva = ListaReproduccion(f"{self._nombre} + {otra_lista.nombre}")
        nueva._canciones = self._canciones + otra_lista.canciones
        lista_fusionada = list(dict.fromkeys(nueva._canciones))
        return lista_fusionada

    def __sub__(self, cancion): #Eliminar una canción de una lista de reproducción
        if cancion in self._canciones:
           self._canciones.remove(cancion)
        return self

    def __len__(self): #Función para saber cuantas canciones hay en la playlist
        return len(self._canciones)

    def __str__(self):
        return f"Playlist: {self._nombre} [{len(self)} canciones]"