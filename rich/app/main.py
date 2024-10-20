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

def agregar_acabado_o_vidrio():
    agregar = Prompt.ask("[bold yellow]¿Desea agregar un nuevo acabado o tipo de vidrio?[/bold yellow]", choices=["S", "N"]).lower() == 's'
    while agregar:
        opcion = Prompt.ask("[bold cyan]¿Qué desea agregar?[/bold cyan]", choices=["Acabado", "Vidrio"])

        if opcion == "Acabado":
            nombre_acabado = Prompt.ask("[bold green]Ingrese el nombre del nuevo acabado[/bold green]")
            precio_acabado = float(Prompt.ask("[bold blue]Ingrese el precio del nuevo acabado por metro lineal[/bold blue]"))
            Ventana.agregar_nuevo_acabado(nombre_acabado, precio_acabado)
            console.print(f"[bold green]Acabado {nombre_acabado} agregado con éxito[/bold green]")

        elif opcion == "Vidrio":
            nombre_vidrio = Prompt.ask("[bold green]Ingrese el nombre del nuevo tipo de vidrio[/bold green]")
            precio_vidrio = float(Prompt.ask("[bold blue]Ingrese el precio del nuevo tipo de vidrio por cm²[/bold blue]"))
            Ventana.agregar_nuevo_vidrio(nombre_vidrio, precio_vidrio)
            console.print(f"[bold green]Vidrio {nombre_vidrio} agregado con éxito[/bold green]")

        agregar = Prompt.ask("[bold yellow]¿Desea agregar otro acabado o tipo de vidrio?[/bold yellow]", choices=["S", "N"]).lower() == 's'

def crear_cotizacion():
    header_text = Text("Sistema de Cotización", style="bold white on blue", justify="center")
    console.print(Panel(header_text, border_style="bold blue", padding=(1, 1)))

    es_empresa = Prompt.ask("[bold yellow]¿El cliente es una empresa?[/bold yellow]", choices=["S", "N"]).lower() == 's'
    nombre_cliente = Prompt.ask("[bold cyan]Ingrese el nombre del cliente[/bold cyan]")

    empresa_cliente = None
    if es_empresa:
        empresa_cliente = Prompt.ask("[bold blue]Ingrese el nombre de la empresa[/bold blue]")

    direccion_contacto = Prompt.ask("[bold orange]Ingrese la dirección de contacto[/bold orange]")
    cantidad_modelos = int(Prompt.ask("[bold red]¿Cuántos modelos de ventanas diferentes desea cotizar?[/bold red]"))

    cliente = Cliente(nombre_cliente, es_empresa, empresa_cliente, direccion_contacto, cantidad_modelos)

    # Llamar a la función para agregar nuevos acabados o tipos de vidrio
    agregar_acabado_o_vidrio()

    ventanas = []
    total_ventanas = 0  # Lleva el conteo total de ventanas

    for modelo in range(1, cantidad_modelos + 1):
        console.print(Panel(f"[bold cyan]Configuración del Modelo de Ventana {modelo}[/bold cyan]", border_style="cyan"))

        estilo = Prompt.ask("[bold blue]Ingrese el estilo de la ventana[/bold blue]", choices=["O", "XO", "OXXO", "OXO"])
        ancho = float(Prompt.ask("[bold yellow]Ingrese el ancho de la ventana (cm)[/bold yellow]"))
        alto = float(Prompt.ask("[bold green]Ingrese el alto de la ventana (cm)[/bold green]"))
        acabado = Prompt.ask("[bold orange]Ingrese el tipo de acabado[/bold orange]", choices=list(Ventana.PRECIOS_ACABADO.keys()))
        tipo_vidrio = Prompt.ask("[bold red]Ingrese el tipo de vidrio[/bold red]", choices=list(Ventana.PRECIOS_VIDRIO.keys()))
        esmerilado = Prompt.ask("[bold pink]¿Esmerilado?[/bold pink]", choices=["S", "N"]).lower() == 's'
        
        cantidad_ventanas_modelo = int(Prompt.ask(f"[bold red]¿Cuántas ventanas del modelo {modelo} desea cotizar?[/bold red]"))
        total_ventanas += cantidad_ventanas_modelo

        ventana = Ventana(estilo=estilo, ancho=ancho, alto=alto, acabado=acabado, tipo_vidrio=tipo_vidrio, cantidad=cantidad_ventanas_modelo, esmerilado=esmerilado)
        ventanas.append(ventana)

    cotizacion = Cotizacion(cliente, ventanas)

    precio_total_sin_descuento = cotizacion.calcular_total()
    descuento = 0
    if total_ventanas > 100:
        descuento = 0.10
        precio_total_con_descuento = precio_total_sin_descuento * (1 - descuento)
    else:
        precio_total_con_descuento = precio_total_sin_descuento

    table = Table(title="[bold green]Cotización Final[/bold green]", show_header=True, header_style="bold yellow")
    table.add_column("[bold blue]Descripción[/bold blue]", justify="center")
    table.add_column("[bold cyan]Valor[/bold cyan]", justify="center")

    table.add_row("[bold red]Cliente[/bold red]", cliente.nombre)
    table.add_row("[bold red]Total de Modelos[/bold red]", str(cantidad_modelos))
    table.add_row("[bold red]Total de Ventanas[/bold red]", str(total_ventanas))

    for i, ventana in enumerate(ventanas, start=1):
        precio_por_modelo = ventana.calcular_precio_total()
        table.add_row(f"[bold blue]Modelo {i} - Cantidad: {ventana.cantidad}[/bold blue]", f"${precio_por_modelo:.2f}")

    table.add_row("[bold orange]Precio Total (Sin Descuento)[/bold orange]", f"${precio_total_sin_descuento:.2f}")
    
    if descuento > 0:
        table.add_row("[bold pink]Descuento Aplicado[/bold pink]", f"10%")
        table.add_row("[bold pink]Precio Total (Con Descuento)[/bold pink]", f"${precio_total_con_descuento:.2f}")
    else:
        table.add_row("[bold pink]Precio Total[/bold pink]", f"${precio_total_sin_descuento:.2f}")

    console.print(table)

# Ejecutar el programa
crear_cotizacion()
