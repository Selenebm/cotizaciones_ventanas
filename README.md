# Sistema de Cotización de Ventanas para la Compañía PQR

## Descripción

Este proyecto consiste en el desarrollo de un sistema de cotización de ventanas para la empresa PQR, con el fin de automatizar su proceso manual. El sistema permite calcular el costo total de las ventanas basándose en el estilo de la ventana, tipo de vidrio, acabado de aluminio y otros componentes adicionales.

## Características
- Cálculo de costos para diferentes estilos de ventanas (O, XO, OXXO, OXO).
- Tipos de vidrios y acabados de aluminio.
- Inclusión de componentes adicionales como esquinas y chapas.
- Aplicación de descuentos para pedidos superiores a 100 ventanas.
- Generación de cotización detallada.

from ventana import Ventana
from cotizacion import cotizacion

# Crear algunas ventanas de ejemplo
ventanas = [
    Ventana(estilo="XO", ancho=150, alto=120, acabado="Lacado Brillante", tipo_vidrio="Transparente", esmerilado=True),
    Ventana(estilo="O", ancho=200, alto=180, acabado="Pulido", tipo_vidrio="Bronce", esmerilado=False),
]

# Realizar la cotización
cotizacion(ventanas)


## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local:

1. Clona este repositorio:
    ```bash
    git clone https://github.com/Selenebm/cotizaciones_ventanas.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd proyecto-cotizacion-ventanas
    ```

3. Asegúrate de tener Python instalado en tu sistema. Luego, ejecuta el script principal del proyecto:
    ```bash
    python main.py
    ```

¡Y eso es todo! Ahora puedes comenzar a cotizar ventanas usando el sistema.
