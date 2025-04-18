# OptiBot
 OptiBot – SEO IA Analyzer
OptiBot es una aplicación web construida con Streamlit y la API de OpenAI que permite analizar de forma automática el SEO de cualquier página web. Obtén insights sobre títulos, descripciones, encabezados, imágenes, enlaces y recomendaciones de mejora generadas por IA.

🚀 Características

Análisis de contenido: Título, meta descripción, encabezados H1 y conteo de palabras.

Revisión de imágenes: Número total de imágenes y detección de aquellas sin alt text.

Detección de enlaces: Conteo y listado de enlaces internos y externos.

Sugerencias con IA: Evaluación y recomendaciones de SEO generadas por GPT-3.5 / GPT-4.

Fallback de modelo: Si el modelo seleccionado no está disponible, reintenta automáticamente con gpt-3.5-turbo.

Gestión de credenciales: Genera y carga tu API key de OpenAI en un archivo .env de forma segura.

🛠️ Requisitos

Python 3.8 o superior

Una clave de API válida de OpenAI

Conexión a internet

📦 Instalación

Clona el repositorio

git clone https://github.com/LuisGabrielMelo/OptiBot.git
cd optibot

Crea y activa un entorno virtual

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows

Instala las dependencias

pip install -r requirements.txt

🔑 Configuración de variables de entorno

Asegúrate de contar con el archivo .env en la raíz (se crea automáticamente la primera vez que ejecutas la app).

Define tu API Key de OpenAI:

OPENAI_API_KEY=sk-...tu_clave...

Verifica que .env está incluido en .gitignore para no subirlo al repositorio.

▶️ Cómo ejecutar

streamlit run optibot.py

Abre el navegador en la URL que indica Streamlit (por defecto http://localhost:8501).

Ingresa la URL de la página a analizar.

Selecciona el modelo (gpt-4 o gpt-3.5-turbo).

Haz clic en Analizar y obtén el reporte SEO.

📚 Uso

Ingresa la URL completa de la página (ej. https://tusitio.com).

Elige el modelo de IA.

Revisa los datos encontrados y las sugerencias generadas:

Calidad del contenido y recomendaciones de títulos/meta/H1.

Palabra clave principal.

Optimización de imágenes.

Estrategia de enlaces.

🧩 Estructura del proyecto

optibot/
├── optibot.py         # Lógica principal de la app
├── requirements.txt   # Dependencias del proyecto
├── .env               # Variables de entorno (no en Git)
└── .gitignore         # Archivos ignorados por Git

🤝 Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de abrir issues o pull requests para mejorar funciones, corregir bugs o añadir documentación.

