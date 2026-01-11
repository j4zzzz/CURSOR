# CURSOR

# Proyecto Final: Python + Cursor AI

Este repositorio contiene el entregable final del curso **"Python + Cursor: Smarter Development with AI"** de Santander Open Academy.

## 🎯 Objetivo
El propósito de este código es demostrar la capacidad de utilizar **Cursor (AI Powered IDE)** para acelerar el desarrollo de software, la generación de pruebas y la documentación.

## 🛠 Tecnologías Utilizadas
* **Python**
* **Flask** (Framework web sugerido por la IA para este ejemplo)
* **Cursor IDE** (Modelos GPT-4 y Claude 3.5 Sonnet)

## 🤖 Cómo utilicé Cursor en este proyecto
Siguiendo la metodología del curso ("programar de forma conversacional"), utilicé las siguientes funcionalidades:

1.  **Generación de Código (Cmd+K):**
    * *Prompt:* "Crea una estructura básica de Flask para una API de tareas (ToDo list)."
2.  **Explicación de Código:**
    * Usé el chat para entender cómo funcionaban los decoradores `@app.route`.
3.  **Generación de Tests:**
    * *Prompt:* "Escribe un test unitario con pytest para verificar que el endpoint '/' responde con status 200."
4.  **Corrección de Errores:**
    * Utilicé la función de "Auto-debug" para corregir errores de sintaxis iniciales.

## 🚀 Cómo ejecutar este proyecto

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt