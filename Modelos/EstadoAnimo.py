from .CancionAlegre import CancionAlegre
from .CancionTriste import CancionTriste

class EstadoAnimo: #Creamos una clase EstadoAnimo gestora y privada entre canciones tristes y canciones alegres
    def __init__(self, nombre):
        #Atributos de instancia:
        self.__nombre = nombre
        #Creamos una lista de canciones alegres y canciones tristes vacías
        self.__lista_alegres = []
        self.__lista_tristes = []

    ''' 
    Función para añadir canciones a las listas anteriores
    dependiendo de si son alegres, tristes o su estado de 
    ánimo no corresponde con ninguna de las dos
    '''
    def __iadd__(self, cancion):
        if isinstance(cancion, CancionAlegre):
            self.__lista_alegres.append(cancion)
            print(f" Clasificada como ALEGRE: {cancion.titulo}")
        elif isinstance(cancion, CancionTriste):
            self.__lista_tristes.append(cancion)
            print(f" Clasificada como TRISTE: {cancion.titulo}")
        else:
            print("Neutral: Sin estado de ánimo definido.")

    def listado_canciones(self): #Función que devuelve la lista de canciones alegres y tristes
        print(f"\n--- ESTADO DE ÁNIMO: {self.__nombre} ---")
        #Si en el bucle no encuentra ninguna cancion, devuelve vacío, si encuentra, imprime la lista:
        print("ALEGRES:", [c.titulo for c in self.__lista_alegres] or "Vacío")
        print("TRISTES:", [c.titulo for c in self.__lista_tristes] or "Vacío")