from cliente import Cliente
from ventana import Ventana
from cotizacion import Cotizacion

def crear_cotizacion():
    # Preguntar si es empresa o persona natural
    es_empresa = input("¿El cliente es una empresa (S/N)? ").lower() == 's'
    
    # Pedir datos del cliente
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    
    empresa_cliente = None
    if es_empresa:
        empresa_cliente = input("Ingrese el nombre de la empresa: ")
    
    direccion_contacto = input("Ingrese la dirección de contacto: ")
    cantidad_ventanas = int(input("Ingrese la cantidad de ventanas: "))
    
    # Crear cliente
    cliente = Cliente(nombre_cliente, es_empresa, empresa_cliente, direccion_contacto, cantidad_ventanas)

    # Crear lista de ventanas
    ventanas = []
    for _ in range(cantidad_ventanas):
        estilo = input("Ingrese el estilo de la ventana (O, XO, OXXO, OXO): ")
        ancho = float(input("Ingrese el ancho de la ventana (cm): "))
        alto = float(input("Ingrese el alto de la ventana (cm): "))
        acabado = input("Ingrese el tipo de acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado): ")
        tipo_vidrio = input("Ingrese el tipo de vidrio (Transparente, Bronce, Azul): ")
        esmerilado = input("¿Esmerilado (S/N)? ").lower() == 's'
        
        # Crear objeto Ventana
        ventana = Ventana(estilo= estilo, ancho=ancho, alto=alto, acabado=acabado, tipo_vidrio=tipo_vidrio, cantidad=1, esmerilado= esmerilado)
        ventanas.append(ventana)

    # Crear cotización
    cotizacion = Cotizacion(cliente, ventanas)
    precio_total = cotizacion.calcular_total()
    print(precio_total)
# Ejecutar el programa
crear_cotizacion()