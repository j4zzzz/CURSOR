# Generado con asistencia de Cursor AI
# Objetivo: Crear una API simple con Flask para gestionar tareas

from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada en memoria
tasks = [
    {"id": 1, "title": "Aprender Cursor", "done": True},
    {"id": 2, "title": "Subir proyecto a GitHub", "done": False}
]

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a la API de Tareas creada con Cursor AI"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    # Cursor sugirió usar request.json para manejar la entrada
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json.get('title'),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(debug=True)