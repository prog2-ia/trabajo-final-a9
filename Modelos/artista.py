class Artista:
    def __init__(self, genero, artista, gentilicio, edad, antiguedad):
        self.genero = genero
        self.artista = artista
        self.gentilicio = gentilicio
        self.edad = edad
        self.antiguedad = antiguedad

        def __str__(self):
            return f'Nombre: {self.nombre} - Duracion: {self.duracion} - Genero: {self.genero} - Artista: {self.artista} - Featuring: {self.featuring} - Idioma: {self.Idioma} - Gentilicio: {self.gentilicio}'
        def __repr__(self):
            return f'<{self.nombre} {self.duracion} {self.genero} {self.artista} {self.featuring} {self.idioma} {self.gentilicio}>'

