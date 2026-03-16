# Importamos desde la carpeta "Modelos"
from Modelos.Artista import Artista
from Modelos.Cancion import Cancion
from Modelos.CancionAlegre import CancionAlegre
from Modelos.CancionTriste import CancionTriste
from Modelos.ListaReproduccion import ListaReproduccion
from Modelos.EstadoAnimo import EstadoAnimo
from Modelos.Genero import Genero
from Modelos.ArtistaConocido import ArtistaConocido
from Modelos.ArtistaPocoConocido import ArtistaPocoConocido


def main():
    print("🎵 BIENVENIDO AL GESTOR MUSICAL TIPO SPOTIFY 🎵\n")

    # ==========================================
    # 1. CREACIÓN Y CLASIFICACIÓN DE ARTISTAS
    # ==========================================
    print("--- 1. GESTIÓN DE ARTISTAS (Métodos de Clase) ---")
    artista1 = Artista.clasificar_segun_oyentes("Pop", "Rosalía", "Española", 31, 8, 40000000)
    artista2 = Artista.clasificar_segun_oyentes("Indie", "Pepe Ruiz", "Española", 25, 2, 10000)
    artista3 = Artista.clasificar_segun_oyentes("Trap", "Bad Bunny", "Puertorriqueño", 29, 9, 85000000)

    print(artista1)
    print(artista2)
    print(artista3)

    # ==========================================
    # 2. CREACIÓN DE CANCIONES Y VALIDACIÓN
    # ==========================================
    print("\n--- 2. GESTIÓN DE CANCIONES (Herencia Simple y StaticMethods) ---")
    cancion1 = CancionAlegre("Despechá", 2.6, "Pop", "Rosalía", None, "Español", "Española", 130)
    cancion2 = CancionTriste("Amorfoda", 3.2, "Trap", "Bad Bunny", None, "Español", "Puertorriqueño", "Desamor")
    cancion3 = Cancion("Canción Indie", 4.5, "Indie", "Pepe Ruiz", None, "Español", "Española")

    if Cancion.comprobar_existe_duracion(cancion1.get_duracion()):
        print(f"✅ La canción '{cancion1.get_titulo()}' es válida. Duración: {cancion1.clasificacion_duracion()}")

    print(cancion1)
    print(cancion2)

    # ==========================================
    # 3. LISTAS DE REPRODUCCIÓN (Sobrecarga Operadores)
    # ==========================================
    print("\n--- 3. LISTAS DE REPRODUCCIÓN (Sobrecarga de Operador +) ---")
    lista_fiesta = ListaReproduccion("Fiesta 2024")
    lista_fiesta.anyadir_cancion(cancion1)

    lista_chill = ListaReproduccion("Tarde Lluviosa")
    lista_chill.anyadir_cancion(cancion2)
    lista_chill.anyadir_cancion(cancion3)

    print(f"Lista 1: {lista_fiesta.get_nombre()} tiene {len(lista_fiesta)} canciones.")
    print(f"Lista 2: {lista_chill.get_nombre()} tiene {len(lista_chill)} canciones.")

    lista_mix = lista_fiesta + lista_chill
    print(f"🔥 MIX CREADO: {lista_mix}")

    # ==========================================
    # 4. ESTADOS DE ÁNIMO (Polimorfismo)
    # ==========================================
    print("\n--- 4. RADAR DE ESTADOS DE ÁNIMO ---")
    radar = EstadoAnimo("Radar Emocional")

    radar.anyadir_cancion(cancion1)
    radar.anyadir_cancion(cancion2)
    radar.anyadir_cancion(cancion3)

    print("")
    radar.listado_canciones()

    # ==========================================
    # 5. GESTIÓN DE GÉNEROS (¡Lo que faltaba!)
    # ==========================================
    print("\n--- 5. CLASIFICACIÓN POR GÉNEROS MUSICALES ---")
    gestor_generos = Genero()

    # Imprimimos el __str__ de Genero para ver las categorías disponibles
    print(gestor_generos)

    # Clasificamos nuestras canciones
    print("\nClasificando canciones en la base de datos...")
    gestor_generos.clasificar_cancion(cancion1)  # Se irá a Pop
    gestor_generos.clasificar_cancion(cancion2)  # Se irá a Trap
    gestor_generos.clasificar_cancion(cancion3)  # Como es "Indie", el if-else la mandará a 'Otros'

    # Mostramos el TOP Géneros según tu algoritmo
    print("\n🏆 Top Géneros con más canciones registradas:")
    top_3 = gestor_generos.obtener_top_generos()
    for i, nombre_genero in enumerate(top_3, start=1):
        print(f"  {i}º Lugar: {nombre_genero}")


if __name__ == "__main__":
    main()