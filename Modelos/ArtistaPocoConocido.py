from .Artista import Artista

class ArtistaPocoConocido(Artista):
    def __init__(self, genero, artista, gentilicio, edad, antiguedad, oyentes_mes):
        super().__init__(genero, artista, gentilicio, edad, antiguedad, oyentes_mes)

    def __str__(self):
        return f'[Poco Conocido] {super().__str__()}'

    def __repr__(self):
        return f'<Artista_poco_conocido: {self.artista} | {self.oyentes_mes} oyentes>'

    def obtener_analisis_estatus(self):
        """Calcula métricas de nicho comparando sus oyentes y su antigüedad en la música."""
        media_global = Artista.media_oyentes_mens()
        distancia_media = media_global - self.oyentes_mes

        # Métrica lógica: Oyentes acumulados por año de carrera
        if self.antiguedad > 0:
            rendimiento_anual = self.oyentes_mes / self.antiguedad
        else:
            rendimiento_anual = self.oyentes_mes

        # Clasificamos su tipo de estatus emergente
        if rendimiento_anual > 50000:
            categoria_nicho = "Promesa en Crecimiento Rápido "
        else:
            categoria_nicho = "Proyecto Independiente de Nicho "

        informe = (
            f" --- INFORME DE ESTATUS INDEPENDIENTE:\n"
            f"   - Clasificación de Carrera: {categoria_nicho}\n"
            f"   - Distancia para alcanzar la media global: {distancia_media:,.2f} oyentes\n"
            f"   - Rendimiento estimado por año de carrera: {rendimiento_anual:,.2f} oyentes/año"
        )
        return informe