class Artista:
    def __init__(self, genero, artista, gentilicio, edad, antiguedad):
        self.genero = genero
        self.artista = artista
        self.gentilicio = gentilicio
        self.edad = edad
        self.antiguedad = antiguedad

    def __str__(self):
        return f'Género: {self.genero} - Artista: {self.artista} - Gentilicio: {self.gentilicio} - Edad: {self.edad} - Antiguedad: {self.antiguedad}'
    def __repr__(self):
        return f'<{self.genero} {self.artista} {self.gentilicio} {self.edad} {self.antiguedad}>'

    lista_genero = {
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

    def clasificar_artista(self):
        # Primero se comprueba si el género del artista está en la lista de géneros
        if self.genero in self.lista_genero:
            self.lista_genero[self.genero].append(self) #Si esta se guarda en la lista de su género en el diccionario
            print(f"Artista {self.artista} guardado en {self.genero}")
        else:
            print("Género no encontrado en la lista.")