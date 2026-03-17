from .ArtistaConocido import ArtistaConocido
from .ArtistaPocoConocido import ArtistaPocoConocido


class Artista:
    lista_oyentes_mens = []

    lista_genero = {
        'Trap': [],
        'Reggaeton': [],
        'Pop': [],
        'Rap': [],
        'Rock': [],
        'Techno': [],
        'Clásica': [],
        'Jazz': [],
        'Country': [],
        'Otros': []
    }

    def __init__(self, genero, artista, gentilicio, edad, antiguedad, oyentes_mes):
        self.genero = genero
        self.artista = artista
        self.gentilicio = gentilicio
        self.edad = edad
        self.antiguedad = antiguedad
        self.oyentes_mes = oyentes_mes
        type(self).lista_oyentes_mens.append(oyentes_mes)

    def __str__(self):
        return f'Género: {self.genero} - Artista: {self.artista} - Gentilicio: {self.gentilicio} - Edad: {self.edad} - Antiguedad: {self.antiguedad} - Oyentes/mes: {self.oyentes_mes}'

    def __repr__(self):
        return f'<Artista: {self.artista} | {self.genero} | {self.oyentes_mes} oyentes>'

    def clasificar_artista(self):
        if self.genero in Artista.lista_genero:
            Artista.lista_genero[self.genero].append(self.artista)
        else:
            Artista.lista_genero['Otros'].append(self.artista)
    @classmethod
    def media_oyentes_mens(cls):
        # Evitamos el error de dividir por cero si la lista está vacía
        if not cls.lista_oyentes_mens:
            return 0
        return sum(cls.lista_oyentes_mens) / len(cls.lista_oyentes_mens)

    @classmethod
    def clasificar_segun_oyentes(cls, genero, artista, gentilicio, edad, antiguedad, oyentes_mes):
        media = cls.media_oyentes_mens()
        # Si tiene menos oyentes que la media (y ya hay una media establecida), creamos la clase hija
        if media > 0 and oyentes_mes < media:
            return ArtistaPocoConocido(genero, artista, gentilicio, edad, antiguedad, oyentes_mes)
        else:
            return ArtistaConocido(genero, artista, gentilicio, edad, antiguedad, oyentes_mes)

    def presentacion_artista(self):
        return f"Soy {self.artista}, tengo {self.edad} años y si te gusta el {self.genero} has dado con el artista indicado."