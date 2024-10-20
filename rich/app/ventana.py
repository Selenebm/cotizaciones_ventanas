class Ventana:
    PRECIOS_ACABADO = {
        'Pulido': 50700 / 100,  # Precio por cm lineal
        'Lacado Brillante': 54200 / 100,
        'Lacado Mate': 53600 / 100,
        'Anodizado': 57300 / 100
    }

    PRECIOS_VIDRIO = {
        'Transparente': 8.25,  # Precio por cm²
        'Bronce': 9.15,
        'Azul': 12.75
    }

    COSTO_ESMERILADO = 5.20  # Adicional por cm² si es esmerilado
    COSTO_ESQUINAS = 4310  # Costo fijo por 4 esquinas
    COSTO_CHAPA = 16200  # Costo fijo si hay "X" en el estilo

    def __init__(self, estilo: str, ancho: float, alto: float, acabado: str, tipo_vidrio: str, cantidad: int = 1, esmerilado: bool = False):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.acabado = acabado
        self.tipo_vidrio = tipo_vidrio
        self.cantidad = cantidad
        self.esmerilado = esmerilado

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

    def calcular_area_vidrio(self) -> float:
        """ Calcula el área del vidrio considerando un margen de 3 cm. """
        ancho, _ = self.calcular_ancho_naves()
        return (ancho - 3) * (self.alto - 3)  

    def calcular_perimetro_nave(self):
        ancho, _ = self.calcular_ancho_naves()
        return 2 * ((ancho - 6) + (self.alto - 6))

    def calcular_costo_aluminio(self):
        area_total = self.calcular_perimetro_nave() * self.calcular_ancho_naves()[1]
        return area_total * self.PRECIOS_ACABADO[self.acabado]

    def calcular_costo_vidrio(self) -> float:
        """ Calcula el costo del vidrio basado en el área de todas las naves. """
        area_vidrio = self.calcular_area_vidrio()  * self.calcular_ancho_naves()[1]# Área total del vidrio
        costo_vidrio = area_vidrio * self.PRECIOS_VIDRIO[self.tipo_vidrio]
        if self.esmerilado:
            costo_vidrio += area_vidrio * self.COSTO_ESMERILADO
        return costo_vidrio

    def calcular_costo_esquinas(self) -> float:
        naves_cant = len(self.estilo)
        return (self.COSTO_ESQUINAS * 4) * naves_cant

    def calcular_costo_chapa(self) -> float:
        contador_x = self.estilo.count("X")
        if "X" in self.estilo:
            return self.COSTO_CHAPA * contador_x
        return 0

    def calcular_precio_total(self) -> float:
        """ Calcula el costo total de la ventana. 
        print(f"Costos intermedios:\nVidrio: {self.calcular_costo_vidrio()}\n"
              f"Acabado: {self.calcular_costo_aluminio()}\n"
              f"Esquinas: {self.calcular_costo_esquinas()}\n"
              f"Chapa: {self.calcular_costo_chapa()}")"""
        return (
            self.calcular_costo_aluminio() +
            self.calcular_costo_vidrio() +
            self.calcular_costo_esquinas() +
            self.calcular_costo_chapa()
        ) * self.cantidad

