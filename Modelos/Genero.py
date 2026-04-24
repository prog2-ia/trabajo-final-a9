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

    def clasificar_cancion(self, cancion):
        # Solución al error: usamos la propiedad .genero
        gen = cancion.genero if cancion.genero in self.lista_genero else 'Otros'
        self.lista_genero[gen].append(cancion)

    def obtener_top_generos(self):
        ordenados = sorted(self.lista_genero.items(), key=lambda x: len(x[1]), reverse=True)
        return [nombre for nombre, lista in ordenados if len(lista) > 0][:3]

    def __str__(self):
        generos_disponibles = ", ".join(self.lista_genero.keys())
        return f'Gestor de Géneros Musicales. Categorías: {generos_disponibles}'

    def __repr__(self):
        return f'<Genero: {len(self.lista_genero)} categorías registradas>'

    def _anyadir_genero(self, genero_nuevo):
        if genero_nuevo not in self.lista_genero:
            self.lista_genero[genero_nuevo] = []
            print(f"Género '{genero_nuevo}' añadido con éxito.")
        else:
            print("El género ya existe.")

        return self.lista_genero
