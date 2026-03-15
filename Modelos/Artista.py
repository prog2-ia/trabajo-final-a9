class Artista:
    lista_oyentes_mens =  []
    def __init__(self, genero, artista, gentilicio, edad, antiguedad, oyentes_mes):
        self.genero = genero
        self.artista = artista
        self.gentilicio = gentilicio
        self.edad = edad
        self.antiguedad = antiguedad
        self.oyentes_mes = oyentes_mes
        type(self).lista_oyentes_mens.append(oyentes_mes)

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
        'Techno': [],
        'Clásica': [],
        'Jazz': [],
        'Country': []
    }

    def clasificar_artista(self):
        # Primero se comprueba si el género del artista está en la lista de géneros
        if self.genero in Artista.lista_genero: #Utilizamos Artista antes de nombrar a la lista para que todos los artistas compartan la misma lista
            Artista.lista_genero[self.genero].append(self.artista) #Si está se guarda en la lista de su género en el diccionario

    @classmethod
    def media_oyentes_mens(cls): # Función para obtener la media de oyentes
        return sum(cls.lista_oyentes_mens) / len(cls.lista_oyentes_mens)

    @classmethod
    def clasificar_oyentes_mens(cls, oyentes_mes):
        media = cls.media_oyentes_mens()

        if oyentes_mes < media:
            return Artista_poco_conocido()
