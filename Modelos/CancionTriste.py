from Cancion import Cancion

class CancionTriste(Cancion): # Utilizamos la herencia simple de Cancion
    def __init__(self, cancion, duracion, genero, artista, featuring, idioma, gentilicio, motivo_tristeza):
        # Utilizamos super para recuperar los atributos comunes con la clase Padre
        super().__init__(cancion, duracion, genero, artista, featuring, idioma, gentilicio)
        # Definimos el tributo exclusivo de esta clase
        self.__motivo_tristeza = motivo_tristeza

    @property # Convertimos el atributo motivo en una propiedad
    def motivo(self):
        return self.__motivo_tristeza

    def __str__(self):
        # Uso super para el título de la canción y el artista, lo traigo de la clase padre.
        return f"Canción triste: {super().__str__()} | Motivo: {self.motivo}"