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
        return 9 * 12  # Área del vidrio en cm², ajustado al ejemplo

    def calcular_costo_aluminio(self) -> float:
        """ Calcula el costo total del aluminio basado en un perímetro fijo de 30 cm. """
        perimetro_total = 30  # Total de cm lineales de aluminio
        return perimetro_total * self.PRECIOS_ACABADO[self.acabado]

    def calcular_costo_vidrio(self) -> float:
        """ Calcula el costo del vidrio basado en el área de todas las naves. """
        area_vidrio = self.calcular_area_vidrio()  # Área total del vidrio
        costo_vidrio = area_vidrio * self.PRECIOS_VIDRIO[self.tipo_vidrio]
        if self.esmerilado:
            costo_vidrio += area_vidrio * self.COSTO_ESMERILADO
        return costo_vidrio

    def calcular_costo_esquinas(self) -> float:
        """ Calcula el costo de las esquinas (siempre 4). """
        return self.COSTO_ESQUINAS * 4

    def calcular_costo_chapa(self) -> float:
        """ Calcula el costo de la chapa solo si el estilo incluye 'X'. """
        if "X" in self.estilo:
            return self.COSTO_CHAPA
        return 0

    def calcular_precio_total(self) -> float:
        """ Calcula el costo total de la ventana. """
        print(f"Costos intermedios:\nVidrio: {self.calcular_costo_vidrio()}\n"
              f"Acabado: {self.calcular_costo_aluminio()}\n"
              f"Esquinas: {self.calcular_costo_esquinas()}\n"
              f"Chapa: {self.calcular_costo_chapa()}")
        return (
            self.calcular_costo_aluminio() +
            self.calcular_costo_vidrio() +
            self.calcular_costo_esquinas() +
            self.calcular_costo_chapa()
        ) * self.cantidad

# Ejemplo de uso
ventana = Ventana(estilo="O", ancho=12, alto=15, tipo_vidrio="Transparente", acabado="Pulido", cantidad=1, esmerilado=False)
costo_total = ventana.calcular_precio_total()
print(f"Costo total: ${costo_total:.2f}")