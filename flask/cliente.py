class Cliente:
    def __init__(self, nombre: str, es_empresa: bool, empresa: str, direccion_contacto: str, cantidad_ventanas: int):
        self.nombre = nombre
        self.es_empresa = es_empresa
        self.empresa = empresa if es_empresa else None
        self.direccion_contacto = direccion_contacto
        self.cantidad_ventanas = cantidad_ventanas