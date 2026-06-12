import streamlit as st

st.set_page_config(page_title="Compras Mary", page_icon="🛍️", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #fde2e7;
    }
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #8b3a52 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛍️ Compras Mary")
st.markdown("Catálogo de productos")
st.markdown("---")

productos = [
    {"nombre": "Casaca", "imagenes": ["imagenes/1.jpeg"]},
    {"nombre": "Abrigo", "imagenes": ["imagenes/2.jpeg"]},
    {"nombre": "Abrigo", "imagenes": ["imagenes/3.jpeg"]},
    {"nombre": "Polera", "imagenes": ["imagenes/4.png"]},
    {"nombre": "Polera", "imagenes": ["imagenes/5.png"]},
    {"nombre": "Casaca", "imagenes": ["imagenes/6.jpeg"]},
    {"nombre": "Chaqueta", "imagenes": ["imagenes/7.jpeg"]},
]

cols_por_fila = 3

for i in range(0, len(productos), cols_por_fila):
    fila = productos[i:i + cols_por_fila]
    cols = st.columns(cols_por_fila)
    for col, producto in zip(cols, fila):
        with col:
            st.image(producto["imagenes"][0], use_container_width=True)
            st.subheader(producto["nombre"])
            st.markdown("---")
