class Ventana:
    PRECIOS_ACABADO = {
        'Pulido': 50700 / 100,  # Precio por cm lineal
        'Lacado Brillante': 54200 / 100,
        'Lacado Mate': 53600 / 100,
        'Anodizado': 57300 / 100
    }

    PRECIOS_VIDRIO = {
        'Transparente': 8.25,  # Precio por cm2
        'Bronce': 9.15,
        'Azul': 12.75
    }

    COSTO_ESMERILADO = 5.20  # Adicional por cm2 si es esmerilado
    COSTO_ESQUINAS = 4310  # Costo fijo por 4 esquinas
    COSTO_CHAPA = 16200  # Costo fijo si hay "X" en el estilo

    def __init__(self, estilo: str, ancho: float, alto: float, acabado: str, tipo_vidrio: str, esmerilado: bool = False):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.acabado = acabado
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado
        self.numero_de_naves = self.calcular_ancho_naves()[1]

    def calcular_ancho_naves(self) -> tuple:
        """ Calcula el ancho de cada nave según el estilo. """
        estilo_naves = {
            "O": 1,
            "XO": 2,
            "OXO": 3,
            "OXXO": 4,
        }
        naves = estilo_naves.get(self.estilo, 1)
        return self.ancho / naves, naves

    def calcular_area_naves(self) -> float:
        """ Calcula el área de una nave restando márgenes fijos. """
        ancho_nave, _ = self.calcular_ancho_naves()
        return (ancho_nave - 1.5) * (self.alto - 1.5)

    def calcular_perimetro_nave(self) -> float:
        """ Calcula el perímetro de una nave considerando reducciones fijas. """
        ancho_nave, _ = self.calcular_ancho_naves()
        return 2 * (ancho_nave + self.alto) - 4 * 4  # Margen de 4 cm en total

    def calcular_costo_aluminio(self) -> float:
        """ Calcula el costo total del aluminio basado en el perímetro de todas las naves. """
        perimetro_total = self.calcular_perimetro_nave() * self.numero_de_naves
        return perimetro_total * self.PRECIOS_ACABADO[self.acabado]

    def calcular_costo_vidrio(self) -> float:
        """ Calcula el costo del vidrio basado en el área de todas las naves. """
        area_total = self.calcular_area_naves() * self.numero_de_naves
        costo_vidrio = area_total * self.PRECIOS_VIDRIO[self.tipo_vidrio]
        if self.esmerilado:
            costo_vidrio += area_total * self.COSTO_ESMERILADO
        return costo_vidrio

    def calcular_costo_esquinas(self) -> float:
        """ Calcula el costo de las esquinas (siempre 4). """
        return self.COSTO_ESQUINAS

    def calcular_costo_chapa(self) -> float:
        """ Calcula el costo de la chapa solo si el estilo incluye 'X'. """
        if "X" in self.estilo:
            return self.COSTO_CHAPA
        return 0

    def calcular_costo_total(self) -> float:
        """ Calcula el costo total de una sola ventana. """
        return (
            self.calcular_costo_aluminio() +
            self.calcular_costo_vidrio() +
            self.calcular_costo_esquinas() +
            self.calcular_costo_chapa()
        )