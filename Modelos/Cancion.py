class Cancion:
    def __init__(self, cancion, duracion, genero, artista, featuring, idioma, gentilicio):
        self.cancion = cancion
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

    def clasificacion_duracion(self): # Función que permite clasificar la duración de cada canción
        canciones_segun_duracion = {
            'Corta': [],
            'Media': [],
            'Larga': []
        }

        if self.duracion < 3:
            canciones_segun_duracion['Corta'].append(self.cancion)
        elif  3 <= self.duracion < 5:
            canciones_segun_duracion['Media'].append(self.cancion)
        else:
            canciones_segun_duracion['Larga'].append(self.cancion)