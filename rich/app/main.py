from cliente import Cliente
from ventana import Ventana
from cotizacion import Cotizacion
from rich.console import Console
from rich.prompt import Prompt
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.layout import Layout

console = Console()

def crear_cotizacion():
    # Cabecera estilizada
    header_text = Text("Sistema de Cotización", style="bold white on blue", justify="center")
    console.print(Panel(header_text, border_style="bold blue", padding=(1, 1)))

    # Crear layout
    layout = Layout()
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
        Layout(name="footer", size=3)
    )

    # Panel de creación de cotización
    layout["header"].update(Panel("[bold green]Creación de Cotización[/bold green]", title="Inicio", border_style="green"))

    # Preguntar si es empresa o persona natural
    es_empresa = Prompt.ask("[bold yellow]¿El cliente es una empresa?[/bold yellow]", choices=["S", "N"]).lower() == 's'
    
    # Pedir datos del cliente
    nombre_cliente = Prompt.ask("[bold cyan]Ingrese el nombre del cliente[/bold cyan]")
    
    empresa_cliente = None
    if es_empresa:
        empresa_cliente = Prompt.ask("[bold blue]Ingrese el nombre de la empresa[/bold blue]")
    
    direccion_contacto = Prompt.ask("[bold orange]Ingrese la dirección de contacto[/bold orange]")

    # Preguntar cuántos modelos de ventanas se van a cotizar
    cantidad_modelos = int(Prompt.ask("[bold red]¿Cuántos modelos de ventanas diferentes desea cotizar?[/bold red]"))

    # Crear cliente
    cliente = Cliente(nombre_cliente, es_empresa, empresa_cliente, direccion_contacto, cantidad_modelos)

    # Crear lista de ventanas
    ventanas = []
    total_ventanas = 0  # Lleva el conteo total de ventanas

    for modelo in range(1, cantidad_modelos + 1):
        console.print(Panel(f"[bold cyan]Configuración del Modelo de Ventana {modelo}[/bold cyan]", border_style="cyan"))
        
        estilo = Prompt.ask("[bold blue]Ingrese el estilo de la ventana[/bold blue]", choices=["O", "XO", "OXXO", "OXO"])
        ancho = float(Prompt.ask("[bold yellow]Ingrese el ancho de la ventana (cm)[/bold yellow]"))
        alto = float(Prompt.ask("[bold green]Ingrese el alto de la ventana (cm)[/bold green]"))
        acabado = Prompt.ask("[bold orange]Ingrese el tipo de acabado[/bold orange]", choices=["Pulido", "Lacado Brillante", "Lacado Mate", "Anodizado"])
        tipo_vidrio = Prompt.ask("[bold red]Ingrese el tipo de vidrio[/bold red]", choices=["Transparente", "Bronce", "Azul"])
        esmerilado = Prompt.ask("[bold pink]¿Esmerilado?[/bold pink]", choices=["S", "N"]).lower() == 's'
        
        # Preguntar cuántas ventanas de este modelo se van a cotizar
        cantidad_ventanas_modelo = int(Prompt.ask(f"[bold red]¿Cuántas ventanas del modelo {modelo} desea cotizar?[/bold red]"))

        # Sumar al total de ventanas
        total_ventanas += cantidad_ventanas_modelo

        # Crear las ventanas de este modelo
        ventana = Ventana(estilo=estilo, ancho=ancho, alto=alto, acabado=acabado, tipo_vidrio=tipo_vidrio, cantidad=cantidad_ventanas_modelo, esmerilado=esmerilado)
        ventanas.append(ventana)

    # Crear cotización
    cotizacion = Cotizacion(cliente, ventanas)

    # Calcular el total antes del descuento
    precio_total_sin_descuento = cotizacion.calcular_total()

    # Descuento si hay más de 100 ventanas
    descuento = 0
    if total_ventanas > 100:
        descuento = 0.10  # 10% de descuento
        precio_total_con_descuento = precio_total_sin_descuento * (1 - descuento)
    else:
        precio_total_con_descuento = precio_total_sin_descuento

    # Mostrar cotización
    table = Table(title="[bold green]Cotización Final[/bold green]", show_header=True, header_style="bold yellow")
    table.add_column("[bold blue]Descripción[/bold blue]", justify="center")
    table.add_column("[bold cyan]Valor[/bold cyan]", justify="center")

    # Información del cliente
    table.add_row("[bold red]Cliente[/bold red]", cliente.nombre)
    table.add_row("[bold red]Total de Modelos[/bold red]", str(cantidad_modelos))
    table.add_row("[bold red]Total de Ventanas[/bold red]", str(total_ventanas))

    # Desglose por modelo
    for i, ventana in enumerate(ventanas, start=1):
        precio_por_modelo = ventana.calcular_precio_total()
        table.add_row(f"[bold blue]Modelo {i} - Cantidad: {ventana.cantidad}[/bold blue]", f"${precio_por_modelo:.2f}")

    # Precio total
    table.add_row("[bold orange]Precio Total (Sin Descuento)[/bold orange]", f"${precio_total_sin_descuento:.2f}")
    
    # Si se aplica descuento
    if descuento > 0:
        table.add_row("[bold pink]Descuento Aplicado[/bold pink]", f"10%")
        table.add_row("[bold pink]Precio Total (Con Descuento)[/bold pink]", f"${precio_total_con_descuento:.2f}")
    else:
        table.add_row("[bold pink]Precio Total[/bold pink]", f"${precio_total_sin_descuento:.2f}")

    console.print(table)

# Ejecutar el programa
crear_cotizacion()
