# Biblioteca Musical 

Este proyecto es una simulación de una biblioteca musical, para la elaboración de este proyecto hemos utilizado una arquitectura modular.

# Conceptos de programación orientada a objetos que hemos utilizado 

El proyecto demuestra el dominio de los siguientes pilares de la POO y características avanzadas de Python:

* **Clases Abstractas (ABC):** Uso de `ABC` y `@abstractmethod` en la clase base `Cancion` para obligar a definir el método `reproducir()` en sus hijas.
* **Herencia Especializada:** `CancionAlegre` y `CancionTriste` heredan de `Cancion`.
    * `ArtistaConocido` y `ArtistaPocoConocido` heredan de `Artista`.
* **Encapsulamiento:** Atributos protegidos (`_`) y privados (`__`) con uso de decoradores `@property` para un acceso seguro a los datos.
* **Polimorfismo:** Tratamiento uniforme de diferentes tipos de canciones en las listas de reproducción al ejecutar sus comportamientos específicos.
* **Sobrecarga de Operadores:** Implementación de `__add__` para fusionar playlists y `__sub__` para eliminar canciones de forma intuitiva.
* **Gestión de Excepciones Personalizadas:** Creación y lanzamiento de errores propios (`ErrorMetadatosErroneos`, `ErrorRutaRota`, `ErrorPistaCorrupta`) para asegurar que el programa sea robusto y controle fallos de datos o rutas sin colgarse.
* **Persistencia mediante Serialización Binaria:** Uso de la biblioteca `pickle` combinada con gestores de contexto (`with open`) para guardar y cargar objetos completos en archivos binarios, manteniendo intacta la jerarquía de las canciones grabadas.

## Estructura del Proyecto

El código está organizado de la siguiente manera:

```text
├── Main/
│   ├── __init__.py
│   └── Main.py               # Interfaz de usuario y flujo principal
├── Modelos/                  # Lógica de negocio y entidades
│   ├── __init__.py
│   ├── Album.py              # Gestión de colecciones de canciones
│   ├── Artista.py            # Clase base para artistas
│   ├── ArtistaConocido.py    # Artistas con premios y reconocimiento
│   ├── ArtistaPocoConocido.py # Artistas emergentes
│   ├── Cancion.py            # Clase abstracta base
│   ├── CancionAlegre.py      # Canciones con BPM y ritmo alto
│   ├── CancionTriste.py      # Canciones con motivos melancólicos
│   ├── EstadoAnimo.py        # Gestor de sentimientos de la biblioteca
│   ├── Genero.py             # Clasificador por categorías musicales
│   └── ListaReproduccion.py  # Manejo de playlists y operaciones
├── Persistencia/             # Gestión de archivos y errores del sistema
│   ├── __init__.py
│   ├── Excepciones.py        # Clases de errores personalizados 
│   └── GestorArchivos.py     # Guardado y carga binaria con pickle 
├── Servicios/
│   └── __init__.py
├── UI/
│   └── __init__.py
└── README.md                 # Documentación técnica
```
##  Autores
* Luis Garcia Arroyo
* Denís Mora Mas