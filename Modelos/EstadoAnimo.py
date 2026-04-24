from .CancionAlegre import CancionAlegre
from .CancionTriste import CancionTriste

class EstadoAnimo:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__lista_alegres = []
        self.__lista_tristes = []

    def anyadir_cancion(self, cancion):
        if isinstance(cancion, CancionAlegre):
            self.__lista_alegres.append(cancion)
            print(f" Clasificada como ALEGRE: {cancion.titulo}")
        elif isinstance(cancion, CancionTriste):
            self.__lista_tristes.append(cancion)
            print(f" Clasificada como TRISTE: {cancion.titulo}")
        else:
            print("Neutral: Sin estado de ánimo definido.")

    def listado_canciones(self):
        print(f"\n--- ESTADO DE ÁNIMO: {self.__nombre} ---")
        print("ALEGRES:", [c.titulo for c in self.__lista_alegres] or "Vacío")
        print("TRISTES:", [c.titulo for c in self.__lista_tristes] or "Vacío")