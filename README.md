
# 🚀 OptiBot – SEO IA Analyzer

**OptiBot** es una aplicación web construida con **Streamlit** y la **API de OpenAI** que analiza de forma automática el SEO de cualquier página web. Ofrece insights detallados sobre títulos, descripciones, encabezados, imágenes, enlaces y recomendaciones optimizadas mediante inteligencia artificial.

---

## ✨ Características

- 🔍 **Análisis de contenido**: Extrae título, meta descripción, encabezados `H1` y conteo de palabras.
- 🖼️ **Revisión de imágenes**: Detecta imágenes sin texto alternativo (`alt`) y muestra el total.
- 🔗 **Detección de enlaces**: Lista y clasifica enlaces internos y externos.
- 🤖 **Recomendaciones IA**: Sugerencias SEO generadas por modelos de lenguaje (GPT-3.5 o GPT-4).
- 🔄 **Fallback de modelo**: Cambia automáticamente a GPT-3.5 si GPT-4 no está disponible.
- 🔐 **Gestión segura de credenciales**: Usa archivo `.env` para tu clave API de OpenAI.

---

## 🛠️ Requisitos

- Python 3.8 o superior
- Una clave API válida de OpenAI
- Conexión a internet

---

## 📦 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/LuisGabrielMelo/OptiBot.git
   cd optibot
   ```

2. **Crea y activa un entorno virtual**:
   - macOS / Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Configuración

1. Crea un archivo `.env` en la raíz del proyecto (se crea automáticamente al ejecutar la app por primera vez).
2. Añade tu clave de OpenAI:

   ```env
   OPENAI_API_KEY=sk-...tu_clave...
   ```

3. Asegúrate de que el archivo `.env` está en `.gitignore` para proteger tu clave.

---

## ▶️ Ejecución

Inicia la app con:

```bash
streamlit run optibot.py
```

Luego abre el navegador en la URL que aparece (por defecto: `http://localhost:8501`).

---

## 📚 Uso

1. Ingresa la URL completa del sitio a analizar (ej. `https://tusitio.com`).
2. Selecciona el modelo: `gpt-4` o `gpt-3.5-turbo`.
3. Haz clic en **Analizar**.
4. Visualiza el reporte SEO con:

   - Diagnóstico del contenido.
   - Palabra clave principal detectada.
   - Recomendaciones sobre títulos, descripciones, encabezados.
   - Optimización de imágenes.
   - Estrategia de enlaces internos y externos.

---

## 📁 Estructura del proyecto

```
optibot/
├── optibot.py          # Lógica principal de la app
├── requirements.txt    # Dependencias
├── .env                # Variables de entorno (ignorado por Git)
└── .gitignore          # Exclusiones de Git
```

---

## 🤝 Contribuciones

¡Contribuciones son bienvenidas! Puedes:

- Reportar errores (issues)
- Proponer mejoras
- Enviar pull requests

Ayudemos a mejorar el SEO con IA, ¡juntos!
