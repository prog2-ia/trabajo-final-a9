# Importamos todas las clases desde el paquete Modelos
from Modelos.Artista import Artista
from Modelos.ArtistaConocido import ArtistaConocido
from Modelos.ArtistaPocoConocido import ArtistaPocoConocido
from Modelos.Cancion import Cancion
from Modelos.CancionAlegre import CancionAlegre
from Modelos.CancionTriste import CancionTriste
from Modelos.EstadoAnimo import EstadoAnimo
from Modelos.Genero import Genero
from Modelos.ListaReproduccion import ListaReproduccion


def ejecutar_demo():
    print("--- 1. GESTIÓN DE ARTISTAS ---")
    # Usamos el método de clase para clasificar según oyentes (media)
    # Primero creamos un artista base para establecer una media
    a1 = Artista("Pop", "Dua Lipa", "Británica", 28, 10, 70000000)

    # El método clasificar_segun_oyentes decidirá si es Conocido o Poco Conocido
    a2 = Artista.clasificar_segun_oyentes("Rock", "Banda Local", "Española", 22, 2, 500)

    # Ejemplo de Artista Conocido con premios
    a3 = ArtistaConocido("Trap", "Bad Bunny", "Puertorriqueño", 30, 8, 80000000,
                         ["Grammy Awards", "Billboard Music Awards"])

    print(a1.presentacion_artista())
    print(f"¿Es {a3.artista} internacional? {a3.ser_artista_internacional()}")
    print("-" * 30)

    print("\n--- 2. GESTIÓN DE CANCIONES Y ESTADOS DE ÁNIMO ---")
    # Creamos diferentes tipos de canciones
    cancion1 = CancionAlegre("Happy Song", 3.5, "Pop", "Dua Lipa", None, "Inglés", "Británica", 124)
    cancion2 = CancionTriste("Lonely Night", 4.2, "Jazz", "Banda Local", "Feat. X", "Español", "Española",
                             "Ruptura amorosa")
    cancion3 = Cancion("Generic Track", 2.5, "Techno", "DJ Unknown", None, "Instrumental", "Alemana")

    # Gestionamos el ánimo
    mi_mood = EstadoAnimo("Mix del Día")
    mi_mood.anyadir_cancion(cancion1)
    mi_mood.anyadir_cancion(cancion2)
    mi_mood.anyadir_cancion(cancion3)  # Esta se clasificará como genérica

    print("\n")
    mi_mood.listado_canciones()
    print("-" * 30)

    print("\n--- 3. CLASIFICACIÓN POR GÉNEROS ---")
    gestor_generos = Genero()
    gestor_generos.clasificar_cancion(cancion1)
    gestor_generos.clasificar_cancion(cancion2)

    print(f"Top Géneros actuales: {gestor_generos.obtener_top_generos()}")
    print("-" * 30)

    print("\n--- 4. LISTAS DE REPRODUCCIÓN (PLAYLISTS) ---")
    playlist_verano = ListaReproduccion("Verano 2026")
    playlist_verano.anyadir_cancion(cancion1)

    playlist_relax = ListaReproduccion("Chill Mode")
    playlist_relax.anyadir_cancion(cancion2)

    # Probamos la sobrecarga del operador __add__
    playlist_mix = playlist_verano + playlist_relax

    print(playlist_verano)
    print(playlist_relax)
    print(f"Nueva lista combinada: {playlist_mix}")
    print(f"Total canciones en mix: {len(playlist_mix)}")


if __name__ == "__main__":
    ejecutar_demo()