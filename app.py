import streamlit as st

st.set_page_config(page_title="Compras Mary", page_icon="🛍️", layout="wide")

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

for producto in productos:
    st.subheader(producto["nombre"])
    cols = st.columns(len(producto["imagenes"]))
    for i, img in enumerate(producto["imagenes"]):
        with cols[i]:
            st.image(img, use_container_width=True)
    st.markdown("---")
