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
            'Country': [],
            'Otros': []
        }

    def __str__(self):
        generos_disponibles = ", ".join(self.lista_genero.keys())
        return f'Gestor de Géneros Musicales. Categorías: {generos_disponibles}'

    def __repr__(self):
        return f'<Genero: {len(self.lista_genero)} categorías registradas>'

    def clasificar_cancion(self, cancion):
        # Si el género existe la cancion se introduce en la lista de género que le corresponde
        if cancion.genero in self.lista_genero:
            self.lista_genero[cancion.genero].append(cancion)
        else:
            self.lista_genero['Otros'].append(cancion)
        return self.lista_genero