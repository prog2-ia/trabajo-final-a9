import sys
import os

# Ajuste de ruta para poder importar desde la carpeta "Modelos"
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Modelos.Cancion import Cancion
from Modelos.CancionAlegre import CancionAlegre
from Modelos.CancionTriste import CancionTriste
from Modelos.EstadoAnimo import EstadoAnimo
from Modelos.Genero import Genero


def menu_principal():
    print("\n" + "=" * 50)
    print("       SPOTIFY-CLONE: GESTIÓN MUSICAL ")
    print("=" * 50)
    print("1. Añadir nueva canción (Autoclasificación)")
    print("2. Buscar canciones por Filtros (NUEVO)")
    print("3. Ver Top Géneros y Estado de Ánimo")
    print("4. Salir")
    print("=" * 50)


def ejecutar_biblioteca():
    # Inicializamos nuestros gestores y una lista global para el buscador
    gestor_generos = Genero()
    mi_mood = EstadoAnimo("Mi Radar de Emociones")
    biblioteca_global = []

    # --- DATOS DE PRUEBA PRECARGADOS ---
    c1 = CancionAlegre("Levitating", 3.2, "Pop", "Dua Lipa", "DaBaby", "Inglés", "Británica", 103)
    c2 = CancionTriste("Someone Like You", 4.8, "Pop", "Adele", None, "Inglés", "Británica", "Ruptura")
    c3 = Cancion("Generic Track", 2.1, "Techno", "DJ Unknown", None, "Inglés", "Alemana")
    c4 = CancionAlegre("Despacito", 3.8, "Reggaeton", "Luis Fonsi", "Daddy Yankee", "Español", "Puertorriqueño", 89)

    for c in [c1, c2, c3, c4]:
        biblioteca_global.append(c)
        gestor_generos.clasificar_cancion(c)
        mi_mood.anyadir_cancion(c)

    # --- BUCLE PRINCIPAL ---
    while True:
        menu_principal()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            print("\n--- AÑADIR CANCIÓN ---")
            titulo = input("Título: ")
            artista = input("Artista: ")
            gen = input("Género (Pop, Rock, Reggaeton...): ").capitalize()

            try:
                dur = float(input("Duración en min (ej. 3.5): "))
            except ValueError:
                print(" Error: La duración debe ser un número.")
                continue

            print("\nVamos a analizar la vibra de la canción (Pulsa ENTER para omitir):")
            bpm = input("Si es alegre, introduce los BPM (ritmo): ")

            # Autoclasificación dinámica basada en el input del usuario
            if bpm.strip():
                nueva_cancion = CancionAlegre(titulo, dur, gen, artista, None, "Español", "Desconocido", bpm)
            else:
                motivo = input("Si es melancólica, introduce el motivo de tristeza: ")
                if motivo.strip():
                    nueva_cancion = CancionTriste(titulo, dur, gen, artista, None, "Español", "Desconocido", motivo)
                else:
                    nueva_cancion = Cancion(titulo, dur, gen, artista, None, "Español", "Desconocido")

            # Guardamos en todos los registros
            biblioteca_global.append(nueva_cancion)
            gestor_generos.clasificar_cancion(nueva_cancion)
            mi_mood.anyadir_cancion(nueva_cancion)
            print(f"\n '{nueva_cancion.titulo}' añadida y clasificada correctamente.")

        elif opcion == '2':
            print("\n--- BUSCADOR POR FILTROS ---")
            print(" Deja en blanco (pulsa Enter) los filtros que no quieras usar.")

            f_gen = input("Filtro de Género (ej. Pop, Reggaeton): ").strip().capitalize()
            f_dur = input("Filtro de Duración (Corta / Media / Larga): ").strip().capitalize()
            f_tipo = input("Filtro de Ánimo (Alegre / Triste / Generica): ").strip().capitalize()

            print("\n Resultados de tu búsqueda:")
            resultados = 0

            for c in biblioteca_global:
                coincide = True

                # Comprobación de filtros (Si el usuario escribió algo y no coincide, se descarta)
                if f_gen and c.genero != f_gen:
                    coincide = False

                # Aquí le damos uso al metodo clasificacion_duracion() que no se usaba
                if f_dur and c.clasificacion_duracion() != f_dur:
                    coincide = False

                if f_tipo:
                    if f_tipo == "Alegre" and not isinstance(c, CancionAlegre):
                        coincide = False
                    elif f_tipo == "Triste" and not isinstance(c, CancionTriste):
                        coincide = False
                    elif f_tipo == "Generica" and (isinstance(c, CancionAlegre) or isinstance(c, CancionTriste)):
                        coincide = False

                # Si pasó todos los filtros aplicados, la mostramos
                if coincide:
                    resultados += 1
                    tipo_str = "Alegre" if isinstance(c, CancionAlegre) else "Triste" if isinstance(c,
                                                                                                    CancionTriste) else "Genérica"
                    print(
                        f" - {c.titulo} | Artista: {c.artista} | Duración: {c.clasificacion_duracion()} ({c.duracion}m) | Ánimo: {tipo_str}")

            if resultados == 0:
                print("No se ha encontrado ninguna canción con esos filtros.")
            else:
                print(f"\n  Total encontradas: {resultados}")

        elif opcion == '3':
            print("\n--- ESTADÍSTICAS DE LA BIBLIOTECA ---")
            print("TOP GÉNEROS:")
            tops = gestor_generos.obtener_top_generos()
            for i, g in enumerate(tops, 1):
                print(f" {i}. {g}")

            print("\n📊 BALANCE DE ÁNIMO:")
            mi_mood.listado_canciones()

        elif opcion == '4':
            print("\nSaliendo del reproductor... ¡Hasta la próxima! 🎵")
            break

        else:
            print("\n Opción incorrecta. Introduce un número del 1 al 4.")


if __name__ == "__main__":
    ejecutar_biblioteca()