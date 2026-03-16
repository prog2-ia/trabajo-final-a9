from Artista import Artista

class ArtistaConocido(Artista):  # Herencia simple de la clase Artista
    premiosInternacionales = ['Grammy Awards',
                              'Billboard Music Awards',
                              'World Music Awards',
                              'Polar Music Prize',
                              'Global Music Awards',
                              'International Classical Music Awards',
                              'MTV Europe Music Awards']
    def __init__(self, genero, artista, gentilicio, edad, antiguedad, oyentes_mes, premios=0):
        super().__init__(genero, artista, gentilicio, edad, antiguedad, oyentes_mes) #Utilizamos super para recuperar los atributos de Artista
        # Añadimos premios, ya que este atributo no lo heredamos de Artista
        # Si no pasan nada, self.premios será una lista vacía, no el número 0
        if premios is None:
            self.premios = []
        else:
            self.premios = premios

    def __str__(self):
        return f'[Conocido] {super().__str__()} - Premios: {self.premios}'

    def __repr__(self):
        return f'<ArtistaConocido: {self.artista} | {self.premios} premios>'

    def ser_artista_internacional(self):
        # Comprobamos si alguno de sus premios está en la lista de referencia
        for premio in self.premios:
            if premio in ArtistaConocido.premiosInternacionales:
                return True
        return False

