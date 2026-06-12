import streamlit as st

st.set_page_config(page_title="Compras Mary", page_icon="🛍️", layout="wide")

st.title("🛍️ Compras Mary")
st.markdown("Catálogo de productos")
st.markdown("---")

# ============================================
# AQUÍ AGREGAS TUS PRODUCTOS
# Cada producto es un diccionario con:
# - nombre
# - descripcion
# - categoria
# - imagenes (lista de rutas)
# ============================================

productos = [
    {
        "nombre": "Polerón gris básico",
        "descripcion": "Polerón con capucha, talla S a L, color gris.",
        "categoria": "Polerones",
        "imagenes": ["imagenes/poleron1_1.jpg", "imagenes/poleron1_2.jpg"]
    },
    {
        "nombre": "Abrigo negro largo",
        "descripcion": "Abrigo de invierno, talla M a XL, color negro.",
        "categoria": "Abrigos",
        "imagenes": ["imagenes/abrigo1_1.jpg"]
    },
    # 👆 Copia este formato para agregar más productos
]

# ============================================
# MOSTRAR PRODUCTOS
# ============================================

for producto in productos:
    st.subheader(producto["nombre"])
    st.caption(f"Categoría: {producto['categoria']}")
    st.write(producto["descripcion"])

    # Mostrar galería de imágenes en columnas
    cols = st.columns(len(producto["imagenes"]))
    for i, img in enumerate(producto["imagenes"]):
        with cols[i]:
            st.image(img, use_container_width=True)

    st.markdown("---")
