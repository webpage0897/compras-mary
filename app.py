import streamlit as st

st.set_page_config(page_title="Compras Mary", page_icon="🛍️", layout="wide")

st.title("🛍️ Compras Mary")
st.markdown("Catálogo de productos")
st.markdown("---")

productos = [
    {"nombre": "Casaca", "imagenes": ["imagenes/1.jpg"]},
    {"nombre": "Abrigo", "imagenes": ["imagenes/2.jpg"]},
    {"nombre": "Abrigo", "imagenes": ["imagenes/3.jpg"]},
    {"nombre": "Polera", "imagenes": ["imagenes/4.jpg"]},
    {"nombre": "Polera", "imagenes": ["imagenes/5.jpg"]},
    {"nombre": "Casaca", "imagenes": ["imagenes/6.jpg"]},
    {"nombre": "Chaqueta", "imagenes": ["imagenes/7.jpg"]},
]

for producto in productos:
    st.subheader(producto["nombre"])
    cols = st.columns(len(producto["imagenes"]))
    for i, img in enumerate(producto["imagenes"]):
        with cols[i]:
            st.image(img, use_container_width=True)
    st.markdown("---")
