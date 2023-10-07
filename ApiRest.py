import os
import json
from flask import Flask

# Crea una instancia de Flask
app = Flask(__name__)

# Define una ruta para el recurso `datos`
@app.route("/api/datos", methods=["POST"])

# Define la función que se ejecutará cuando se reciba una petición HTTP al recurso `datos`
def datos():
    # Obtén los datos de la petición
    data = request.json()

    # Procesa los datos
    temperatura = data["temperatura"]
    humedad = data["humedad"]

    # Devuelve una respuesta
    return jsonify({"temperatura": temperatura, "humedad": humedad})

# Configura el servidor para que acepte peticiones HTTP con un encabezado de `Content-Type` de `application/json`
app.config["ALLOWED_HEADERS"] = ["Content-Type"]

# Ejecuta la aplicación
#app.run(host="0.00.00.0", port=8080)
