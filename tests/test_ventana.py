import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ventana import Ventana  

class TestVentana:
    def test_calcular_ancho_naves(self):
        ventana = Ventana(estilo="OXO", ancho=12, alto=15, acabado="Pulido", tipo_vidrio="Transparente")
        ancho_nave, naves = ventana.calcular_ancho_naves()
        assert ancho_nave == 4  # 12 / 3 = 4
        assert naves == 3  # OXO tiene 3 naves

    def test_calcular_area_vidrio(self):
        ventana = Ventana(estilo="O", ancho=12, alto=15, acabado="Pulido", tipo_vidrio="Transparente")
        assert ventana.calcular_area_vidrio() == 108  # Área de 9cm x 12cm = 108cm²

    def test_calcular_costo_aluminio(self):
        ventana = Ventana(estilo="O", ancho=12, alto=15, acabado="Pulido", tipo_vidrio="Transparente")
        assert ventana.calcular_costo_aluminio() == 15210  # 30cm * (50700 / 100)

    def test_calcular_costo_vidrio_transparente(self):
        ventana = Ventana(estilo="O", ancho=12, alto=15, acabado="Pulido", tipo_vidrio="Transparente")
        assert ventana.calcular_costo_vidrio() == 891  # 108cm² * $8.25/cm²

    def test_calcular_costo_vidrio_esmerilado(self):
        ventana = Ventana(estilo="O", ancho=12, alto=15, acabado="Pulido", tipo_vidrio="Transparente", esmerilado=True)
        assert ventana.calcular_costo_vidrio() == 1452.6  # 108cm² * $8.25 + 108cm² * $5.20

    def test_calcular_costo_esquinas(self):
        ventana = Ventana(estilo="O", ancho=12, alto=15, acabado="Pulido", tipo_vidrio="Transparente")
        assert ventana.calcular_costo_esquinas() == 4310 * 4 # Costo fijo por 4 esquinas

    def test_calcular_costo_chapa_con_chapa(self):
        ventana = Ventana(estilo="XO", ancho=12, alto=15, acabado="Pulido", tipo_vidrio="Transparente")
        assert ventana.calcular_costo_chapa() == 16200  # Costo de la chapa

    def test_calcular_costo_chapa_sin_chapa(self):
        ventana = Ventana(estilo="O", ancho=12, alto=15, acabado="Pulido", tipo_vidrio="Transparente")
        assert ventana.calcular_costo_chapa() == 0  # Sin costo de chapa

    def test_calcular_precio_total(self):
        ventana = Ventana(estilo="O", ancho=12, alto=15, acabado="Pulido", tipo_vidrio="Transparente")
        total_esperado = (15210 + 891 + 4310 * 4 + 0)  # Costo total de la ventana
        assert ventana.calcular_precio_total() == total_esperado

if __name__ == "__main__":
    pytest.main()