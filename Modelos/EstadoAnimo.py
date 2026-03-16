from CancionAlegre import CancionAlegre
from CancionTriste import CancionTriste

class EstadoAnimo:
    def __init__(self, nombre):
        # Definimos los atributos de nuestra clase
        self.__nombre = nombre
        self.__lista_alegres = []
        self.__lista_tristes = []

    @property  # Convertimos el atributo nombre en una propiedad
    def nombre(self):
        return self.__nombre

    def anyadir_cancion(self, cancion):
        # Usamos isinstance() que devuelve True si el objeto es de esa clase o de alguna de sus superclases
        if isinstance(cancion, CancionAlegre):
            self.__lista_alegres.append(cancion)
            print(f"Clasificada como ALEGRE: {cancion.get_titulo()}")

        elif isinstance(cancion, CancionTriste):
            self.__lista_tristes.append(cancion)
            print(f"Clasificada como TRISTE: {cancion.get_titulo()}")

        else:
            print("Es una canción genérica sin estado de ánimo definido.")

    def listado_canciones(self):
        print(f"RESUMEN DE LAS CANCIONES")
        print('*'*25)
        print("CANCIONES PARA SUBIR EL ÁNIMO:")
        if len(self.__lista_alegres) == 0:
            print("Lista vacía, no hay ninguna canción alegre todavía")
        else:
            for cancion in self.__lista_alegres:  # Utilizamos for para recorrer la lista
                print(f"  - {cancion}")
        print('*' * 25)

        print("CANCIONES PARA MOMENTOS TRISTES:")
        if len(self.__lista_tristes) == 0:
            print("Lista vacía, no hay ninguna canción triste todavía")
        else:
            for cancion in self.__lista_tristes:
                print(f"  - {cancion}") # Hacemos un print mostrando el nombre de la CancionTriste.

