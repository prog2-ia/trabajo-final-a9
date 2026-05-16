class ListaReproduccion:
    def __init__(self, nombre):
        self._nombre = nombre
        self._canciones = []  # Guardaremos los objetos tipo Cancion

    @property
    def nombre(self):
        return self._nombre

    @property
    def canciones(self):
        # Añadimos este getter para que otra lista pueda leer nuestras canciones al sumar
        return self._canciones

    def anyadir_cancion(self, cancion_nueva):
        from .Cancion import Cancion
        if isinstance(cancion_nueva, Cancion):
            if cancion_nueva not in self._canciones:
                self._canciones.append(cancion_nueva)
        return self

    def __add__(self, otra_lista):  # Con está función vamos a poder combinar dos playlist
        # Creamos la nueva playlist con el nombre de las dos playlist que queremos juntar
        nombre_combinado = f"{self._nombre} + {otra_lista.nombre}"
        nueva_playlist = ListaReproduccion(nombre_combinado)

        # Juntamos las canciones y utilizamos un bucle para eliminar posibles duplicados
        canciones_sin_repetir = []

        for cancion_actual in self._canciones:
            if cancion_actual not in canciones_sin_repetir:
                canciones_sin_repetir.append(cancion_actual)

        # Guardamos el resultado del objeto nuevo
        nueva_playlist._canciones = canciones_sin_repetir
        return nueva_playlist

    def __sub__(self, cancion_a_eliminar):  # Eliminar una canción de una lista de reproducción
        # Creamos una playlist nueva para no modificar la lista original
        nueva_playlist = ListaReproduccion(self._nombre)

        canciones_filtradas = []
        for cancion_actual in self._canciones:
            # Si la canción no es la que queremos borrar, la guardamos
            if cancion_actual != cancion_a_eliminar:
                canciones_filtradas.append(cancion_actual)

        nueva_playlist._canciones = canciones_filtradas
        return nueva_playlist

    def __len__(self):  # Función para saber cuantas canciones hay en la playlist
        return len(self._canciones)

    def __eq__(self, otra_lista):
        # Sobrecargamos el operador '==' y comparamos las dos listas para ver si son iguales
        if isinstance(otra_lista, ListaReproduccion):
            return self._canciones == otra_lista.canciones
        return False

    def __str__(self):
        return f"Playlist: {self._nombre} [{len(self)} canciones]"