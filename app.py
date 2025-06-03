import streamlit as st
from scraper import scrape_products

st.set_page_config(page_title="Scraper Universal", layout="wide")
st.title("🌐 Scraper Universal de Productos")

url = st.text_input("🔗 Ingresá la URL del sitio web (página de productos)")
query = st.text_input("🛍️ ¿Qué producto estás buscando? (por nombre o palabra clave)")

if st.button("Buscar productos"):
    if not url or not query:
        st.warning("Por favor ingresá una URL válida y una palabra clave de producto.")
    else:
        with st.spinner("Buscando productos…"):
            result = scrape_products(url, query)

        if result["success"]:
            st.success(result["message"])
            if not result["products"]:
                st.warning("No se encontraron productos con el nombre buscado.")
            else:
                for i, p in enumerate(result["products"], 1):
                    st.markdown(f"### Producto #{i}")
                    st.write(f"**Nombre**: {p['name']}")
                    st.write(f"**Precio**: {p['price']}")
                    st.write(f"**Disponibilidad**: {p['stock']}")
                    st.markdown("---")
        else:
            st.error(f"Error al hacer scraping: {result['error']}")
