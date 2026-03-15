class ArtistaConocido(Artista):  # Herencia simple de la clase Artista
    def __init__(self, genero, artista, gentilicio, edad, antiguedad, oyentes_mes, premios=0):
        super().__init__(genero, artista, gentilicio, edad, antiguedad, oyentes_mes) #Utilizamos super para recuperar los atributos de Artista

        # Añadimos premios, ya que este atributo no lo heredamos de Artista
        self.premios = premios

    def __str__(self):
        return f'[Conocido] {super().__str__()} - Premios: {self.premios}'

    def __repr__(self):
        return f'<ArtistaConocido: {self.artista} | {self.premios} premios>'