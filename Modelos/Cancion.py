class Cancion:
    def __init__(self, nombre, duracion, genero, artista, featuring, idioma, gentilicio):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.artista = artista
        self.featuring = featuring
        self.idioma = idioma
        self.gentilicio = gentilicio

    def __str__(self):
        return f'Nombre: {self.nombre} - Duracion: {self.duracion} - Genero: {self.genero} - Artista: {self.artista} - Featuring: {self.featuring} - Idioma: {self.Idioma} - Gentilicio: {self.gentilicio}'
    def __repr__(self):
        return f'<{self.nombre} {self.duracion} {self. genero} {self.artista} {self.featuring} {self.idioma} {self.gentilicio}>'