class ListaReproduccion:
    def __init__(self, nombre):
        self._nombre = nombre
        self._canciones = []  # Guardaremos los objetos tipo Cancion

    def get_nombre(self):
        return self._nombre

    def anyadir_cancion(self, cancion): #Añade una canción a la lista
        self._canciones.append(cancion)

    def get_canciones(self): #getter necesario para usar en el add
        return self._canciones

    def __add__(self, otra_lista): # Combinar dos listas distintas
        nombre_nueva_lista = f"{self._nombre} y {otra_lista.get_nombre()}" #Nombre de la lista actual y la otra lista de la cual necesitamos su nombre
        nueva_lista = ListaReproduccion(nombre_nueva_lista) #El nuevo objeto es una lista con el nuevo nombre
        nueva_lista._canciones = self._canciones + otra_lista.get_canciones() #La nueva lista es la suma de una lista y la otra

        return nueva_lista

    def __len__(self): #Función para saber cuantas canciones hay en la playlist
        return len(self._canciones)

    def __str__(self):
        return f"Playlist: {self._nombre} [{len(self)} canciones]"