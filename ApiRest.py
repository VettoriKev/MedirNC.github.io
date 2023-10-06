# Importa Flask
from flask import Flask
import requests

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

# Ejecuta la aplicación
app.run()
