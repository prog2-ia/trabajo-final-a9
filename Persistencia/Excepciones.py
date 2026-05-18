class ErrorBibliotecaMusical(Exception):
    """Clase base para las excepciones de nuestra aplicación"""
    pass

class ErrorRutaRota(ErrorBibliotecaMusical):
    """Se lanza cuando el archivo .pkl o de texto no se encuentra o no es accesible"""
    def __init__(self, ruta, mensaje="La ruta especificada no existe o está rota"):
        self.ruta = ruta
        self.mensaje = f"{mensaje}: '{ruta}'"
        super().__init__(self.mensaje)

class ErrorPistaCorrupta(ErrorBibliotecaMusical):
    """Se lanza cuando los datos de una canción están dañados o el formato de Pickle falla"""
    def __init__(self, detalle, mensaje="La pista musical está corrupta o dañada"):
        self.detalle = detalle
        self.mensaje = f"{mensaje} ({detalle})"
        super().__init__(self.mensaje)

class ErrorMetadatosErroneos(ErrorBibliotecaMusical):
    """Se lanza cuando los atributos de una canción no son válidos"""
    def __init__(self, campo, valor, mensaje="Metadatos erróneos en el formato de la pista"):
        self.campo = campo
        self.valor = valor
        self.mensaje = f"{mensaje} -> El campo '{campo}' no puede tener el valor: {valor}"
        super().__init__(self.mensaje)