# 🕷️ Universal Web Scraper

Este proyecto permite ingresar una URL y un producto buscado para obtener automáticamente una lista de productos coincidentes en la página, extrayendo:
- Nombre del producto
- Precio
- Disponibilidad
- Stock (si está disponible)

Funciona con múltiples sitios web y utiliza procesamiento de lenguaje natural (NLP) para mejorar la extracción de precios y productos, incluso si la estructura HTML es variable.

---

## 🚀 ¿Cómo usar?

### 🌐 En Streamlit Cloud (Recomendado para producción)

1. Cloná este repositorio o hacé fork si lo vas a modificar.
2. Asegurate de que en tu repositorio esté el archivo `postinstall.sh`.
3. Subí el proyecto a [Streamlit Cloud](https://streamlit.io/cloud) desde tu GitHub.
4. Streamlit ejecutará `postinstall.sh` automáticamente para descargar el modelo de spaCy necesario (`en_core_web_sm`).

✅ Ya podés ingresar una URL, el nombre de producto y ver los resultados extraídos automáticamente.

---

### 💻 Para correr localmente

#### 1. Clonar el repositorio
```bash
git clone https://github.com/carlosconsigli/universal-scraper.git
cd universal-scraper
