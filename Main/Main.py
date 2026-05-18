import os
import sys

# Subimos un nivel para encontrar la raíz del proyecto (donde están Modelos y Persistencia)
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_raiz)

# Importaciones de tu modelo
from Modelos.CancionAlegre import CancionAlegre
from Modelos.CancionTriste import CancionTriste
from Modelos.EstadoAnimo import EstadoAnimo
from Modelos.Genero import Genero
from Modelos.ListaReproduccion import ListaReproduccion
from Modelos.Artista import Artista
from Modelos.ArtistaConocido import ArtistaConocido
from Modelos.ArtistaPocoConocido import ArtistaPocoConocido

# Importaciones de persistencia y excepciones
from Persistencia.Excepciones import ErrorMetadatosErroneos, ErrorPistaCorrupta, ErrorRutaRota
from Persistencia.GestorArchivos import GestorArchivos

FICHERO_BIBLIOTECA = "biblioteca_musical.pkl"


def mostrar_menu():
    print("\n" + "=" * 50)
    print("        🎵 SPOTIFY-CLONE: GESTOR DE BIBLIOTECA 🎵")
    print("=" * 50)
    print(" 1. Ver mi Lista de Reproducción")
    print(" 2. Añadir nueva canción (Vincular/Crear Artista)")
    print(" 3. Buscar canciones por filtros")
    print(" 4. Ver Estadísticas (Top Géneros y Balance de Ánimo)")
    print(" 5. Demostración de Sobrecarga (Combinar con otra Playlist +)")
    print(" 6. Ver Clasificaciones Avanzadas (Canciones y Artistas)")
    print(" 7. Guardar y Salir")
    print("=" * 50)


def inicializar_gestores(playlist):
    """Puebla los gestores y la base de datos de artistas ficticia basándose en la playlist."""
    gestor_generos = Genero()
    mi_mood = EstadoAnimo("Mi Radar de Emociones")
    base_artistas = {}  # Diccionario: { "nombre_artista": objeto_artista }

    # Primero poblamos los oyentes para que la media de la clase Artista calcule bien
    if not Artista.lista_oyentes_mens:
        Artista.lista_oyentes_mens.extend([500000, 15000000])  # Valores de referencia iniciales

    # Re-creamos objetos artista para las canciones existentes
    for cancion in playlist.canciones:
        gestor_generos.clasificar_cancion(cancion)
        mi_mood += cancion

        if cancion.artista not in base_artistas:
            base_artistas[cancion.artista] = ArtistaConocido(
                cancion.genero, cancion.artista, "Británica", 30, 5, 25000000, ["Grammy Awards"]
            )

    return gestor_generos, mi_mood, base_artistas


def main():
    print(" Iniciando el sistema y cargando base de datos...")
    try:
        playlist_global = GestorArchivos.cargar_playlist(FICHERO_BIBLIOTECA)
        print(f" Éxito: Se han cargado {len(playlist_global)} canciones guardadas.")
    except ErrorRutaRota:
        print("ℹ No se encontró archivo previo. Creando una biblioteca nueva vacía.")
        playlist_global = ListaReproduccion("Mis Favoritas de Siempre")

        try:
            c1 = CancionAlegre("Levitating", 3.2, "Pop", "Dua Lipa", "DaBaby", "Inglés", "Británica", 103)
            c2 = CancionTriste("Someone Like You", 4.5, "Pop", "Adele", None, "Inglés", "Británica", "Ruptura amorosa")
            playlist_global += c1
            playlist_global += c2
        except ErrorMetadatosErroneos:
            pass
    except ErrorPistaCorrupta as e:
        print(f" Alerta: El archivo estaba dañado ({e.detalle}). Iniciando biblioteca vacía.")
        playlist_global = ListaReproduccion("Mis Favoritas (Recuperada)")

    # Inicializar componentes
    gestor_generos, mi_mood, base_artistas = inicializar_gestores(playlist_global)

    while True:
        mostrar_menu()
        opcion = input(" Selecciona una opción (1-7): ").strip()

        if opcion == '1':
            print(f"\n LISTA DE REPRODUCCIÓN: '{playlist_global.nombre}'")
            print(f"Total: {len(playlist_global)} canciones.")
            print("-" * 50)
            if not playlist_global.canciones:
                print("  (La lista está vacía actualmente)")
            for i, c in enumerate(playlist_global.canciones, 1):
                art_obj = base_artistas.get(c.artista)
                tag_artista = "[Conocido]" if isinstance(art_obj, ArtistaConocido) else "[Emergente]" if art_obj else ""
                print(f" {i}. {c} {tag_artista}")

        elif opcion == '2':
            print("\n➕ AÑADIR NUEVA CANCIÓN Y REGISTRAR ARTISTA")
            titulo = input("Título: ")
            artista_input = input("Nombre del Artista: ").strip()
            featuring = input("Featuring (Pulsa ENTER si ninguno): ")
            featuring = featuring if featuring else None
            genero_input = input("Género (Pop, Rock, Reggaeton, Techno, etc.): ").strip().capitalize()
            idioma = input("Idioma: ")
            gentilicio = input("Gentilicio del artista: ")

            try:
                duracion = float(input("Duración en minutos: "))
            except ValueError:
                print(" Error: La duración debe ser un número entero o decimal.")
                continue

            # --- VINCULACIÓN CON LA CLASE ARTISTA ---
            if artista_input not in base_artistas:
                print(f"\n🎤 El artista '{artista_input}' no está registrado en el sistema.")
                print("Por favor, introduce sus datos de perfil para darlo de alta:")
                try:
                    edad = int(input("   Edad del artista: "))
                    antiguedad = int(input("   Años de antigüedad en la música: "))
                    oyentes = int(input("   Oyentes mensuales en Spotify: "))
                except ValueError:
                    print(" Datos numéricos inválidos. Cancelando registro de canción.")
                    continue

                # La factoría decide automáticamente basándose en la media actual
                nuevo_artista_obj = Artista.clasificar_segun_oyentes(
                    genero_input, artista_input, gentilicio, edad, antiguedad, oyentes
                )

                if isinstance(nuevo_artista_obj, ArtistaConocido):
                    tiene_premio = input("¿Tiene algún premio internacional importante? (S/N): ").strip().upper()
                    if tiene_premio == 'S':
                        print("Premios válidos:", ArtistaConocido.premiosInternacionales)
                        p = input("Escribe el nombre exacto del premio: ").strip()
                        nuevo_artista_obj.premios = [p]

                base_artistas[artista_input] = nuevo_artista_obj
                print(f" Perfil de Artista creado con éxito: {type(nuevo_artista_obj).__name__}")

            tipo_animo = input("\n¿Qué vibra tiene la canción? (1: Alegre / 2: Triste): ").strip()

            try:
                if tipo_animo == '1':
                    try:
                        bpm = int(input("Pulsaciones por minuto (BPM): "))
                    except ValueError:
                        bpm = 120
                    nueva_cancion = CancionAlegre(titulo, duracion, genero_input, artista_input, featuring, idioma,
                                                  gentilicio, bpm)
                elif tipo_animo == '2':
                    motivo = input("Motivo de la tristeza: ")
                    nueva_cancion = CancionTriste(titulo, duracion, genero_input, artista_input, featuring, idioma,
                                                  gentilicio, motivo)
                else:
                    print(" Error: Debes clasificar el ánimo (1 o 2).")
                    continue

                playlist_global += nueva_cancion
                mi_mood += nueva_cancion
                gestor_generos.clasificar_cancion(nueva_cancion)
                print(f"🎵 ¡'{nueva_cancion.titulo}' añadida y vinculada correctamente!")

            except ErrorMetadatosErroneos as e:
                print(f"\n ERROR DE VALIDACIÓN: {e.mensaje}")

        elif opcion == '3':
            print("\n BUSCADOR CON FILTROS AVANZADOS")
            print("Deja en blanco (ENTER) si no quieres aplicar un filtro.")
            f_artista = input("Filtrar por Artista: ").strip().lower()
            f_genero = input("Filtrar por Género: ").strip().lower()
            f_tipo = input("Tipo (Alegre / Triste): ").strip().capitalize()

            print("\n RESULTADOS DE LA BÚSQUEDA:")
            resultados = 0
            for c in playlist_global.canciones:
                coincide = True
                if f_artista and f_artista not in c.artista.lower(): coincide = False
                if f_genero and f_genero != c.genero.lower(): coincide = False
                if f_tipo:
                    if f_tipo == "Alegre" and not isinstance(c, CancionAlegre):
                        coincide = False
                    elif f_tipo == "Triste" and not isinstance(c, CancionTriste):
                        coincide = False

                if coincide:
                    resultados += 1
                    tipo_str = "Alegre" if isinstance(c, CancionAlegre) else "Triste"
                    print(
                        f" - {c.titulo} | Artista: {c.artista} | Duración: {c.clasificacion_duracion()} ({c.duracion}m) | Ánimo: {tipo_str}")

            if resultados == 0:
                print("No se encontró ninguna canción con esos criterios.")
            else:
                print(f"\nTotal encontradas: {resultados}")

        elif opcion == '4':
            print("\n ESTADÍSTICAS DE TU BIBLIOTECA")
            print("Top 3 Géneros más escuchados:")
            tops = gestor_generos.obtener_top_generos()
            if not tops: print("  No hay suficientes géneros registrados todavía.")
            for i, g in enumerate(tops, 1): print(f"  {i}. {g}")
            mi_mood.listado_canciones()

        elif opcion == '5':
            print("\n DEMOSTRACIÓN: SOBRECARGA DEL OPERADOR (+)")
            playlist_festivales = ListaReproduccion("Hits de Verano")
            try:
                c_fest1 = CancionAlegre("Don't Start Now", 3.0, "Pop", "Dua Lipa", None, "Inglés", "Británica", 124)
                c_fest2 = CancionAlegre("Blinding Lights", 3.3, "Synthwave", "The Weeknd", None, "Inglés", "Canadiense",
                                        171)
                playlist_festivales += c_fest1
                playlist_festivales += c_fest2
            except ErrorMetadatosErroneos:
                pass

            playlist_combinada = playlist_global + playlist_festivales
            print(f"\n ¡Operación realizada con éxito (`+`)!")
            print(f"Nueva Playlist Resultante: '{playlist_combinada.nombre}'")
            for i, c in enumerate(playlist_combinada.canciones, 1):
                print(f"   [{i}] {c.titulo} - {c.artista}")

        elif opcion == '6':
            print("\n SECCIÓN DE CLASIFICACIONES AVANZADAS")
            print(" ¿Qué clasificación deseas consultar?")
            print("  1. Por Duración de Canción")
            print("  2. Por Estado de Ánimo")
            print("  3. Por Género Musical")
            print("  4. Ver Fichas e Informes Reales de ARTISTAS")

            sub_opcion = input("👉 Selecciona un criterio (1-4): ").strip()

            if sub_opcion == '1':
                print("\n CLASIFICACIÓN POR DURACIÓN:")
                criterio_duracion = input("Introduce la categoría (Corta / Media / Larga): ").strip().capitalize()
                print(f"\n Canciones con duración [{criterio_duracion}]:")
                encontradas = False
                for c in playlist_global.canciones:
                    if c.clasificacion_duracion() == criterio_duracion:
                        print(f"  - {c.titulo} ({c.duracion} min) - {c.artista}")
                        encontradas = True
                if not encontradas: print(f"  No se encontraron canciones.")

            elif sub_opcion == '2':
                mi_mood.listado_canciones()

            elif sub_opcion == '3':
                print("\n CLASIFICACIÓN COMPLETA POR GÉNERO:")
                vacio = True
                for genero_nombre, canciones_en_genero in gestor_generos.lista_genero.items():
                    if canciones_en_genero:
                        vacio = False
                        print(f"\n• Género: {genero_nombre}")
                        for titulo_cancion in canciones_en_genero: print(f" {titulo_cancion}")
                if vacio: print("  Aún no hay canciones clasificadas.")

            elif sub_opcion == '4':
                print("\n BASE DE DATOS DE ARTISTAS DEL SISTEMA:")
                print(f"Media global de oyentes actuales: {Artista.media_oyentes_mens():,.2f} oyentes/mes\n")

                for nombre, artista_obj in base_artistas.items():
                    print("-" * 60)
                    print(artista_obj)

                    if isinstance(artista_obj, ArtistaConocido):
                        es_internacional = "SÍ " if artista_obj.ser_artista_internacional() else "NO "
                        print(f" Análisis de Estatus: ¿Es de nivel internacional?: {es_internacional}")

                    elif isinstance(artista_obj, ArtistaPocoConocido):
                        #  Ejecutamos el nuevo metodo de análisis de rendimiento estadístico en lugar del consejo
                        print(artista_obj.obtener_analisis_estatus())

        elif opcion == '7':
            print("\n Guardando biblioteca en disco...")
            try:
                GestorArchivos.guardar_playlist(playlist_global, FICHERO_BIBLIOTECA)
            except ErrorRutaRota as e:
                print(f" No se pudieron guardar los cambios: {e.mensaje}")
            print("\n🎵 ¡Gracias por usar Spotify-Clone! ¡Hasta la próxima! ")
            break
        else:
            print(" Opción no válida. Por favor, introduce un número del 1 al 7.")


if __name__ == "__main__":
    main()