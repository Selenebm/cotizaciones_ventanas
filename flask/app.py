from flask import Flask, render_template, request
from ventana import Ventana
from cotizacion import Cotizacion
from cliente import Cliente

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def cotizar():
    if request.method == "POST":
        # Datos del cliente
        nombre_cliente = request.form["nombre_cliente"]
        es_empresa = "es_empresa" in request.form
        empresa = request.form.get("empresa", "") if es_empresa else None
        direccion_contacto = request.form["direccion_contacto"]

        # Crear lista de ventanas
        ventanas = []
        cantidad_ventanas = int(request.form["cantidad_ventanas"])

        for i in range(cantidad_ventanas):
            estilo = request.form[f"estilo_{i}"]
            ancho = float(request.form[f"ancho_{i}"])
            alto = float(request.form[f"alto_{i}"])
            acabado = request.form[f"acabado_{i}"]
            tipo_vidrio = request.form[f"tipo_vidrio_{i}"]
            cantidad = int(request.form[f"cantidad_{i}"])
            esmerilado = f"esmerilado_{i}" in request.form

            ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, cantidad, esmerilado)
            ventanas.append(ventana)

        # Crear objeto Cliente
        cliente = Cliente(nombre_cliente, es_empresa, empresa, direccion_contacto, cantidad_ventanas)

        # Crear la cotización
        cotizacion = Cotizacion(cliente, ventanas)
        costo_total = cotizacion.calcular_total()

        return render_template("cotizador.html", resultado=costo_total, cotizacion=cotizacion)

    return render_template("cotizador.html")

if __name__ == "__main__":
    app.run(debug=True)
