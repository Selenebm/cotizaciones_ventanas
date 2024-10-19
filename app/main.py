from cliente import Cliente
from ventana import Ventana
from cotizacion import Cotizacion
from rich.console import Console
from rich.prompt import Prompt
from rich import print
from rich.panel import Panel
from rich.table import Table

console = Console()

def crear_cotizacion():
    console.print(Panel("[bold green]Creación de Cotización[/bold green]"))

    # Preguntar si es empresa o persona natural
    es_empresa = Prompt.ask("[bold yellow]¿El cliente es una empresa?[/bold yellow]", choices=["S", "N"]).lower() == 's'
    
    # Pedir datos del cliente
    nombre_cliente = Prompt.ask("[bold cyan]Ingrese el nombre del cliente[/bold cyan]")
    
    empresa_cliente = None
    if es_empresa:
        empresa_cliente = Prompt.ask("[bold blue]Ingrese el nombre de la empresa[/bold blue]")
    
    direccion_contacto = Prompt.ask("[bold orange]Ingrese la dirección de contacto[/bold orange]")
    cantidad_ventanas = int(Prompt.ask("[bold red]Ingrese la cantidad de ventanas[/bold red]"))

    # Crear cliente
    cliente = Cliente(nombre_cliente, es_empresa, empresa_cliente, direccion_contacto, cantidad_ventanas)

    # Crear lista de ventanas
    ventanas = []
    for i in range(1, cantidad_ventanas + 1):
        console.print(f"[bold cyan]Ventana {i}[/bold cyan]")
        estilo = Prompt.ask("[bold blue]Ingrese el estilo de la ventana[/bold blue]", choices=["O", "XO", "OXXO", "OXO"])
        ancho = float(Prompt.ask("[bold yellow]Ingrese el ancho de la ventana (cm)[/bold yellow]"))
        alto = float(Prompt.ask("[bold green]Ingrese el alto de la ventana (cm)[/bold green]"))
        acabado = Prompt.ask("[bold orange]Ingrese el tipo de acabado[/bold orange]", choices=["Pulido", "Lacado Brillante", "Lacado Mate", "Anodizado"])
        tipo_vidrio = Prompt.ask("[bold red]Ingrese el tipo de vidrio[/bold red]", choices=["Transparente", "Bronce", "Azul"])
        esmerilado = Prompt.ask("[bold pink]¿Esmerilado?[/bold pink]", choices=["S", "N"]).lower() == 's'

        # Crear objeto Ventana
        ventana = Ventana(estilo= estilo, ancho=ancho, alto=alto, acabado=acabado, tipo_vidrio=tipo_vidrio, cantidad=1, esmerilado= esmerilado)
        ventanas.append(ventana)

    # Crear cotización
    cotizacion = Cotizacion(cliente, ventanas)
    precio_total = cotizacion.calcular_total()

    # Mostrar cotización
    table = Table(title="[bold green]Cotización Final[/bold green]", show_header=True, header_style="bold yellow")
    table.add_column("[bold blue]Descripción[/bold blue]", justify="center")
    table.add_column("[bold cyan]Valor[/bold cyan]", justify="center")
    table.add_row("[bold red]Cliente[/bold red]", cliente.nombre)
    table.add_row("[bold orange]Cantidad de Ventanas[/bold orange]", str(cantidad_ventanas))
    table.add_row("[bold pink]Precio Total[/bold pink]", f"${precio_total:.2f}")
    
    console.print(table)

# Ejecutar el programa
crear_cotizacion()
