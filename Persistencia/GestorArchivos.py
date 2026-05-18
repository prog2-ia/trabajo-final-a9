# Implementamos una herecia sobre excepciones y añadimos pickle

import pickle
from Excepciones import ErrorRutaRota, ErrorPistaCorrupta


class GestorArchivos:
    """
    Clase encargada de la persistencia de las listas de reproduccion
    Implementa la serializacion binaria con pickle y gestion de excepciones
    """

    @staticmethod
    def guardar_playlist(playlist, ruta_del_archivo):
        """
        Almacena el objeto playlist completo en un archivo binario
        """
        # Guardamos en una variable el modo de escritura binaria ('w' de write, 'b' de binario)
        modo_escritura_binario = 'wb'

        try:
            # Abrimos el archivo de forma segura. El archivo se cerrará solo al cabar
            with open(ruta_del_archivo, modo_escritura_binario) as fichero_abierto:
                # Guardamos la playlist entera dentro del archivo binario
                pickle.dump(playlist, fichero_abierto)

            print(f"Confirmacion: Lista '{playlist.nombre}' guardada con exito.")

        except OSError:
            # Si el sistema no nos deja escribir el archivo por falta de permisos o ruta rota salta un excepción, no se pudo escribir el archivo
            raise ErrorRutaRota(ruta_del_archivo, "No se pudo escribir el archivo binario en el disco")

    @staticmethod
    def cargar_playlist(ruta_del_archivo):
        """
        Primero lee el archivo guardado y vuelve a
        montar la lista en el programa con todas sus canciones alegres y tristes intactas
        """
        # Guardamos en una variable el modo de lectura binaria ('r' de read, 'b' de binary)
        modo_lectura_binario = 'rb'

        try:
            # Abrimos el archivo en modo lectura binaria
            with open(ruta_del_archivo, modo_lectura_binario) as fichero_abierto:
                # Recuperamos el objeto playlist tal y como estaba en memoria
                playlist_recuperada = pickle.load(fichero_abierto)
            return playlist_recuperada

        except FileNotFoundError:
            # Definimos una excepción por si el usuario introduce el nombre de un archivo que no exista en la carpeta
            raise ErrorRutaRota(ruta_del_archivo, "El archivo binario solicitado no existe")

        except (pickle.UnpicklingError, EOFError):
            # Definimos una excepción por si el archivo existe pero se corto o alguien lo modifico y esta dañado
            raise ErrorPistaCorrupta(ruta_del_archivo, "El archivo binario esta corrupto o incompleto")