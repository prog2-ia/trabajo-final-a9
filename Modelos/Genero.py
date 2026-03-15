class Genero:
    def __init__(self):
        self.lista_genero = {
            'Trap': [],
            'Reggaeton': [],
            'Pop': [],
            'Rap': [],
            'Rock': [],
            'Techno': [],
            'Clásica': [],
            'Jazz': [],
            'Country': []
        }

    def __str__(self):
        generos_disponibles = ", ".join(self.lista_genero.keys())
        return f'Gestor de Géneros Musicales. Categorías: {generos_disponibles}'

    def __repr__(self):
        return f'<Genero: {len(self.lista_genero)} categorías registradas>'

    def clasificar_cancion(self, cancion):
        # Comprobamos usando el atributo 'genero' del objeto cancion
        if cancion.genero in self.lista_genero:
            self.lista_genero[cancion.genero].append(cancion.cancion)
            return (f"Canción '{cancion.cancion}' del artista {cancion.artista} guardada correctamente en {cancion.genero}.")
        else:
            return(f"Error: El género '{cancion.genero}' no se encuentra en la lista.")