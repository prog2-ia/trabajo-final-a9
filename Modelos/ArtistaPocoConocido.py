class ArtistaPocoConocido(Artista):
    def __init__(self, genero, artista, gentilicio, edad, antiguedad, oyentes_mes):
        super().__init__(genero, artista, gentilicio, edad, antiguedad, oyentes_mes) # Parámetros propios de la clase Artisa

    def __str__(self):
        return f'[Poco Conocido] {super().__str__()}'

    def __repr__(self):
        return f'<Artista_poco_conocido: {self.artista} | {self.oyentes_mes} oyentes>'
