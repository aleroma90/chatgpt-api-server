from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Reemplazá esta línea con tu API key personal (nunca la compartas públicamente)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.get_json()
    mensaje = data.get("mensaje", "")

    if not mensaje:
        return jsonify({"error": "No se recibió ningún mensaje"}), 400

    try:
        respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                 messages=[{
                                                     "role": "user",
                                                     "content": mensaje
                                                 }])
        return jsonify(
            {"respuesta": respuesta["choices"][0]["message"]["content"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def index():
    return "Servidor funcionando correctamente."


# Puerto que Replit necesita para exponer públicamente
app.run(host="0.0.0.0", port=81)
