import streamlit as st
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import re
import os
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse, urljoin

# --- CREAR .env SI NO EXISTE
env_path = Path(".env")
if not env_path.exists():
    st.warning("🔐 No se encontró el archivo .env. Vamos a crearlo.")
    api_key_input = st.text_input("Ingresa tu OpenAI API Key (sk-...)", type="password")
    if api_key_input:
        with open(".env", "w") as f:
            f.write(f"OPENAI_API_KEY={api_key_input.strip()}")
        st.success("✅ Archivo .env creado correctamente. Vuelve a ejecutar la app.")
        st.stop()

# --- CARGAR LA API KEY
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("❌ No se pudo cargar la API Key. Verifica el archivo .env.")
    st.stop()

# --- INICIAR CLIENTE OPENAI
try:
    client = OpenAI(api_key=api_key)
except Exception as e:
    st.error("❌ Error al inicializar el cliente de OpenAI. Verifica tu API Key.")
    st.stop()

# --- CONFIGURACIÓN DE LA APP
st.set_page_config(page_title="SEO IA Analyzer", page_icon="📈", layout="centered")
st.title("🔎 SEO AI Analyzer")
st.markdown("Ingresa una URL y obtén un análisis SEO + sugerencias de mejora generadas con IA.")

# --- INPUTS
url = st.text_input("🌐 URL de la página", placeholder="https://tusitio.com")
modelo = st.selectbox("🤖 Elige el modelo de IA", ["gpt-4", "gpt-3.5-turbo"])

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme in ['http', 'https'], result.netloc])
    except:
        return False

def clasificar_enlace(href, dominio_base):
    if not href or not href.startswith(('http', '/')):
        return None
    enlace = urljoin(f"https://{dominio_base}", href)
    return 'interno' if dominio_base in enlace else 'externo'

if st.button("Analizar"):
    if not url:
        st.warning("⚠️ Por favor, ingresa una URL válida.")
        st.stop()
    if not is_valid_url(url):
        st.warning("🔗 La URL no es válida. Asegúrate de que comience con http:// o https://")
        st.stop()

    try:
        with st.spinner("🔍 Analizando página..."):
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            resp = requests.get(url, headers=headers, timeout=20, verify=True, allow_redirects=True)
            if resp.status_code != 200:
                st.error(f"❌ Error al acceder a la página. Código: {resp.status_code}")
                st.stop()

            resp.encoding = resp.apparent_encoding
            soup = BeautifulSoup(resp.text, "html.parser")

            # --- Datos básicos ---
            try:
                title = soup.title.string.strip() if soup.title and soup.title.string else "Sin título"
            except AttributeError:
                title = "Sin título"

            try:
                meta = soup.find("meta", {"name": "description"}) or soup.find("meta", {"property": "og:description"})
                meta_desc = meta["content"].strip() if meta and meta.get("content") else "Sin metadescripción"
            except (AttributeError, TypeError):
                meta_desc = "Sin metadescripción"

            h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all("h1")]

            texto = soup.get_text()
            palabras = re.findall(r'\w+', texto)
            conteo = len(palabras)
            contenido = ' '.join(palabras[:500])
            contenido = re.sub(r'[^a-zA-Z0-9\s.,áéíóúñÁÉÍÓÚÑ]', '', contenido)

            # --- Imágenes ---
            imgs = soup.find_all("img")
            total_imgs = len(imgs)
            imgs_sin_alt = [img for img in imgs if not img.get("alt")]

            # --- Enlaces ---
            dominio = urlparse(url).netloc
            enlaces = soup.find_all("a", href=True)
            internos, externos = [], []
            for a in enlaces:
                tipo = clasificar_enlace(a['href'], dominio)
                if tipo == 'interno':
                    internos.append(a['href'])
                elif tipo == 'externo':
                    externos.append(a['href'])

            # --- Mostrar resultados ---
            st.subheader("📋 Datos encontrados")
            st.markdown(f"**Título:** {title}")
            st.markdown(f"**Meta descripción:** {meta_desc}")
            st.markdown(f"**H1s:** {', '.join(h1_tags) or 'Ninguno encontrado'}")
            st.markdown(f"**Palabras en la página:** {conteo}")
            st.markdown(f"**Imágenes encontradas:** {total_imgs}")
            st.markdown(f"**Imágenes sin alt text:** {len(imgs_sin_alt)}")
            st.markdown(f"**Enlaces internos:** {len(internos)}")
            st.markdown(f"**Enlaces externos:** {len(externos)}")

            if externos:
                st.markdown("**🔗 Backlinks externos (top 5):**")
                for link in externos[:5]:
                    st.markdown(f"- {link}")

            # --- Prompt extendido para IA ---
            prompt = f"""
Actúa como un experto en SEO. Analiza estos datos de la página:
Título: {title}
Meta descripción: {meta_desc}
H1s: {h1_tags}
Total de palabras: {conteo}
Imágenes totales: {total_imgs}
Imágenes sin alt text: {len(imgs_sin_alt)}
Enlaces internos: {len(internos)}
Enlaces externos: {len(externos)}

Ofrece:
1. Evaluación general para SEO.
2. Mejora de título, descripción y H1s.
3. Palabra clave principal.
4. Recomendaciones de contenido.
5. Optimizar uso de imágenes.
6. Estrategia de enlaces internos/externos.
"""

            respuesta = client.chat.completions.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )

            st.subheader("💡 Sugerencias con IA")
            st.write(respuesta.choices[0].message.content)

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error al acceder a la página: {e}")
    except Exception as e:
        st.error(f"❌ Error inesperado: {e}")
