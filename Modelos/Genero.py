from .Cancion import Cancion

class Genero: #Clase aislada que utiliza objetos de otras clases para  
    def __init__(self):
        self.lista_genero = {
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
    def clasificar_cancion(self, cancion): #Función para clasificar el genero de una canción y añadirlo a la lista que le corresponde
        if isinstance(cancion, Cancion): #Si cancion coincide con un objeto de Cancion se cumple la condición
            if cancion.genero in self.lista_genero: #Se tiene que cumplir que el género de la canción corresponda con alguno del diccionario
                self.lista_genero[cancion.genero].append(cancion.titulo) #Añadimos el titulo al genero correspondiente
            else:
                self.lista_genero['Otros'].append(cancion.titulo) #En caso de que no esté el género en el diccionario, se añadirá a 'otros'



    def obtener_top_generos(self):
        ordenados = sorted(self.lista_genero.items(), key=lambda x: len(x[1]), reverse=True)
        return [nombre for nombre, lista in ordenados if len(lista) > 0][:3]

    def __str__(self):
        generos_disponibles = ", ".join(self.lista_genero.keys())
        return f'Gestor de Géneros Musicales. Categorías: {generos_disponibles}'

    def __repr__(self):
        return f'<Genero: {len(self.lista_genero)} categorías registradas>'

    def _anyadir_genero(self, genero_nuevo):
        if genero_nuevo not in self.lista_genero:
            self.lista_genero[genero_nuevo] = []
            print(f"Género '{genero_nuevo}' añadido con éxito.")
        else:
            print("El género ya existe.")

        return self.lista_genero
