class Cancion:
    def __init__(self, cancion, duracion, genero, artista, featuring, idioma, gentilicio):
        self.cancion = cancion
        self.duracion = duracion
        self.genero = genero
        self.artista = artista
        self.featuring = featuring # En caso de no ser featuring, None o dejar vacío
        self.idioma = idioma
        self.gentilicio = gentilicio

    def __str__(self):
        return f'Nombre: {self.cancion} - Duracion: {self.duracion} min - Genero: {self.genero} - Artista: {self.artista} - Featuring: {self.featuring} - Idioma: {self.idioma}'

    def __repr__(self):
        return f'<Cancion: {self.cancion} | {self.artista} | {self.duracion} min>'

    def clasificacion_duracion(self): #
        if self.duracion < 3:
            return 'Corta'
        elif 3 <= self.duracion < 5:
            return 'Media'
        else:
            return 'Larga'

    def es_colaboracion(self):
        # Si featuring no es None, es una colaboración
        return bool(self.featuring)