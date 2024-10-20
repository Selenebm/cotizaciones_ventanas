from datetime import datetime
class Cotizacion:
    def __init__(self, cliente, ventanas):
        self.cliente = cliente
        self.ventanas = ventanas
        self.fecha = datetime.now()
        self.numero_de_cotizacion = f"COT-{self.fecha.strftime('%Y%m%d%H%M%S')}"
        self.descuento = 0.10 if len(ventanas) > 100 else 0  # Descuento si aplica

    def calcular_total(self):
        costo_total = 0
        for ventana in self.ventanas:
            costo_total += ventana.calcular_precio_total()

        if self.descuento > 0:
            costo_total *= (1 - self.descuento)

        print(f"Nombre del cliente: {self.cliente.nombre}")
        if self.cliente.es_empresa:
            print(f"Empresa: {self.cliente.empresa}")
        print(f"Dirección de contacto: {self.cliente.direccion_contacto}")
        print(f"Fecha de cotización: {self.fecha.strftime('%d-%m-%Y')}")
        print(f"Número de cotización: {self.numero_de_cotizacion}")
        print(f"Descuento aplicado: {self.descuento * 100}%")
        print(f"Costo total: ${costo_total:,.2f}")
        
        return costo_total