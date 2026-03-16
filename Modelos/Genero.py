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
        # Usamos el get para obtener el género de la canción
        genero_cancion = cancion.get_genero()

        if genero_cancion in self.lista_genero:
            self.lista_genero[genero_cancion].append(cancion)
        else:
            self.lista_genero['Otros'].append(cancion)
        return self.lista_genero

    def obtener_top_generos(self):
        # Ordena el diccionario basándose en la longitud de las listas de canciones
        generos_ordenados = sorted(self.lista_genero.items(), key=lambda x: len(x[1]), reverse=True)
        # Devuelve solo el nombre de los géneros que tienen al menos 1 canción
        top_generos = []
        for nombre, lista_cancion in generos_ordenados:
            if len(lista_cancion) > 0: # Si existe almenos una canción en x género
                top_generos.append(nombre)
        return top_generos[:3]

    def _anyadir_genero(self, genero_nuevo):
        if genero_nuevo not in self.lista_genero:
            self.lista_genero[genero_nuevo] = []
            print(f"Género '{genero_nuevo}' añadido con éxito.")
        else:
            print("El género ya existe.")

        return self.lista_genero