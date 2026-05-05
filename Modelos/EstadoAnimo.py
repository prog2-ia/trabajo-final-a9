from .CancionAlegre import CancionAlegre
from .CancionTriste import CancionTriste

class EstadoAnimo: #Creamos una clase EstadoAnimo gestora y privada entre canciones tristes y canciones alegres
    def __init__(self, nombre):
        #Atributos de instancia:
        self.__nombre = nombre
        #Creamos una lista de canciones alegres y canciones tristes vacías
        self.__lista_alegres = []
        self.__lista_tristes = []

    def anyadir_cancion(self, cancion): #Función para añadir canciones a las listas anteriores
        if isinstance(cancion, CancionAlegre): #Si nuestra canción es un objeto de CancionAlegre, se cumple la condición
            self.__lista_alegres.append(cancion) #Añadimos la canción que queremos en la lista de canciones alegres
            print(f" Clasificada como ALEGRE: {cancion.titulo}") #Pequeño mensaje que indica que la lista se ha actualizado
        elif isinstance(cancion, CancionTriste): #Si nuestra canción es un objeto de CancionTriste, se cumple la condición
            self.__lista_tristes.append(cancion) #Añadimos la canción que queremos en la lista de canciones tristes
            print(f" Clasificada como TRISTE: {cancion.titulo}")
        else:
            print("Neutral: Sin estado de ánimo definido.") #Si el estado de ánimo de una canción no corresponde con nignuno o no ha sido definido aún

    def listado_canciones(self): #Función que devuelve la lista de canciones alegres y tristes
        print(f"\n--- ESTADO DE ÁNIMO: {self.__nombre} ---")
        #Si en el bucle no encuentra ninguna cancion, devuelve vacío, si encuentra, imprime la lista:
        print("ALEGRES:", [c.titulo for c in self.__lista_alegres] or "Vacío")
        print("TRISTES:", [c.titulo for c in self.__lista_tristes] or "Vacío")