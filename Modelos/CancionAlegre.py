from Cancion import Cancion

class CancionAlegre(Cancion): # Utilizamos la herencia simple de Cancion
    def __init__(self, cancion, duracion, genero, artista, featuring, idioma, gentilicio, pulsaciones_minuto):
        # Utilizamos super para recuperar los atributos comunes con la clase Padre
        super().__init__(cancion, duracion, genero, artista, featuring, idioma, gentilicio)
        # Definimos las pulsaciones por minuto de la canción ya que es un atriuto exclusivo de esta clase
        self.__pulsaciones_minuto = pulsaciones_minuto

    @property # Convertimos el atributo pulsaciones por minuto en una propiedad.
    def bpm(self):
        return self.__pulsaciones_minuto

    def __str__(self):
        # Uso super para el título de la canción y el artista, lo traigo de la clase padre
        return f"Canción Alegre: {super().__str__()} | Ritmo: {self.__pulsaciones_minuto} BPM"