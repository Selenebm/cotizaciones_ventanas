# Requerimientos del Sistema de Cotización de Ventanas

Este documento especifica los requerimientos funcionales y no funcionales del sistema de cotización de ventanas para la empresa PQR.

## Registro de Entidades

- El sistema debe permitir el registro de un **estilo de ventana** con los siguientes atributos:
  - Tipo de ventana (O, XO, OXXO, OXO).
  - Dimensiones (ancho y alto).
  - Número de naves.
- El sistema debe calcular automáticamente el tamaño de cada nave (panel), basándose en las dimensiones de la ventana completa y su estilo. Por ejemplo, una ventana XO debe dividir su ancho en dos naves: una fija (O) y una móvil (X).
- El sistema debe permitir el registro de una **nave** con los siguientes atributos:
  - Tipo de nave (O o X).
  - Dimensiones (ancho y alto).
  - Tipo de vidrio (transparente, bronce, azul).
  - Acabado de aluminio (pulido, lacado brillante, lacado mate, anodizado).
  - Especificar si el vidrio es esmerilado.
- El sistema debe tener en cuenta que las naves (paneles) tienen un perfil de aluminio de 2.5 cm de ancho, y las esquinas tienen 4 cm, donde se insertan los perfiles. Estos perfiles deben restarse del total del marco.
- El sistema debe permitir el registro de un **tipo de vidrio** con los siguientes atributos:
  - Tipo de vidrio (transparente, bronce, azul).
  - Precio por cm².
  - Costo adicional por vidrio esmerilado.
- El sistema debe permitir el registro de un **acabado de aluminio** con los siguientes atributos:
  - Tipo de acabado (pulido, lacado brillante, lacado mate, anodizado).
  - Precio por metro lineal.
- El sistema debe incluir en el costo del aluminio los materiales adicionales como tornillos, remaches y caucho para insertar el vidrio.
- El sistema debe permitir el registro de **elementos adicionales** con los siguientes atributos:
  - Precio de las esquinas (por unidad).
  - Precio de las chapas (por unidad), aplicable solo a naves tipo X.
- El sistema debe permitir el registro de un **cliente** con los siguientes atributos:
  - Nombre del cliente.
  - Tipo de cliente (por ejemplo, empresa constructora).
  - Dirección de contacto.
- El sistema debe permitir el registro de una **cotización** con los siguientes atributos:
  - Fecha de la cotización.
  - Número de cotización.
  - Cliente asociado.
  - Listado de ventanas y sus especificaciones.
  - Descuento si corresponde.

## Gestión de Precios

- El sistema debe calcular el costo de cada ventana basándose en:
  - **Precio del aluminio**: calculado por metro lineal según el acabado seleccionado. El costo se obtiene sumando los lados de las naves (restando el tamaño de las esquinas).
  - **Precio del vidrio**: calculado por cm² según el tipo de vidrio (transparente, bronce, azul). El tamaño del vidrio debe ser 1.5 cm más pequeño que las dimensiones de la nave en cada lado.
  - **Costo adicional por vidrio esmerilado** si aplica.
  - **Precio de las esquinas**: se requiere una esquina por cada unión de perfiles, con un costo fijo por unidad.
  - **Precio de la chapa**: aplicable solo a las naves tipo X (naves móviles).
- El sistema debe aplicar un **descuento del 10%** si la cantidad de ventanas solicitadas excede las 100 unidades.

## Relaciones entre Entidades

- El sistema debe permitir asociar múltiples **estilos de ventanas** a un cliente.
- El sistema debe relacionar **naves con ventanas**, calculando automáticamente sus dimensiones basadas en el ancho y alto de la ventana completa.
- El sistema debe asociar un **tipo de vidrio** y un **acabado** a cada nave.
- El sistema debe calcular automáticamente el número de **esquinas** y **chapas** necesarias para cada ventana según el tipo y cantidad de naves.

## Consultas y Reportes

- El sistema debe permitir consultar la información de una **ventana**, incluyendo tipo, dimensiones (ancho y alto), número de naves, tipo de vidrio, acabado, y costo total.
- El sistema debe permitir consultar la información de un **cliente**, incluyendo nombre, tipo de cliente, y cotizaciones solicitadas.
- El sistema debe permitir consultar las **cotizaciones realizadas**, incluyendo cliente, fecha de la cotización, y costo total.
- El sistema debe generar **informes de cotización**, detallando el desglose de costos por ventana y aplicando descuentos si corresponde.

## Validaciones

- El sistema debe verificar que las **dimensiones de las naves** sean coherentes con el ancho y alto de la ventana.
- El sistema debe garantizar que el **vidrio** sea siempre 1.5 cm más pequeño que la nave en cada lado.
- El sistema debe asegurar que el **descuento** solo se aplique para más de 100 ventanas del mismo diseño.

## Cálculo de Costos

El sistema debe calcular el costo total de una ventana teniendo en cuenta los siguientes elementos:

1. **Costo del aluminio**:
   - El costo se calcula en base a la longitud total del perfil de aluminio utilizado para el marco de las naves.
   - Fórmula:
     - `costo_aluminio = (largo_perfil_total * precio_por_metro_lineal)`.
     - El largo del perfil total es la suma de los lados de cada nave (ancho + alto), multiplicado por el número de naves, menos las esquinas.

2. **Costo del vidrio**:
   - El vidrio se calcula por cm² para cada nave, restando 1.5 cm a cada lado del vidrio para que encaje en el marco.
   - Fórmula:
     - `costo_vidrio = (ancho_vidrio * alto_vidrio * precio_por_cm2)`.
     - Donde `ancho_vidrio = ancho_nave - 3 cm` y `alto_vidrio = alto_nave - 3 cm` para cada nave.
   - Si el vidrio es esmerilado, se debe agregar el costo adicional por cm².
     - `costo_vidrio_esmerilado = (ancho_vidrio * alto_vidrio * costo_adicional_esmerilado)`.

3. **Costo de las esquinas**:
   - Cada nave necesita 4 esquinas para unir los perfiles del marco.
   - Fórmula:
     - `costo_esquinas = numero_naves * 4 * precio_por_esquina`.

4. **Costo de las chapas**:
   - Para cada nave tipo X, se debe incluir el costo de una chapa.
   - Fórmula:
     - `costo_chapa = numero_naves_X * precio_por_chapa`.

5. **Costo total**:
   - El costo total de la ventana es la suma de los costos de aluminio, vidrio, esquinas y chapas.
   - Fórmula:
     - `costo_total = costo_aluminio + costo_vidrio + costo_esquinas + costo_chapa`.

6. **Descuento por volumen**:
   - Si la cantidad total de ventanas solicitadas excede las 100 unidades, el sistema debe aplicar un descuento del 10%.
   - Fórmula:
     - `costo_final = costo_total * 0.90` (si aplica descuento).

El sistema debe permitir que estos cálculos se realicen de forma automática según las dimensiones ingresadas y los materiales seleccionados por el cliente.

