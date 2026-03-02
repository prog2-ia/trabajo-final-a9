class Genero:
    def __init__(self):
        self.lista_genero = {
        'Trap': [],
        'Reggaeton': [],
        'Pop': [],
        'Rap': [],
        'Rock': [],
        'Tecnho': [],
        'Clásica': [],
        'Jazz': [],
        'Country': []
        }

    def clasificar_cancion(self, cancion):
        # Primero se comprueba si el género del artista está en la lista de géneros
        if self.genero in self.lista_genero:
            self.lista_genero[self.genero].append(self) #Si esta se guarda en la lista de su género en el diccionario
            print(f"Artista {self.artista} guardado en {self.genero}")
        else:
            print("Género no encontrado en la lista.")