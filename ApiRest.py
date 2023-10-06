# Importa Flask
from flask import Flask
import requests

# Crea una instancia de Flask
app = Flask(MedData)

# Define una ruta para el recurso `datos`
@app.route("/api/datos", methods=["POST"], description="Envía datos")

# Define la función que se ejecutará cuando se reciba una petición HTTP al recurso `datos`
def datos():
    # Obtén los datos de la petición
    data = request.json()

    # Procesa los datos
    temperatura = data["temperatura"]
    humedad = data["humedad"]

    # Devuelve una respuesta
    return jsonify({"temperatura": temperatura, "humedad": humedad}, content_type="application/json")

# Ejecuta la aplicación
app.run()
