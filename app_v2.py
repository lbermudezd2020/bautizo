import streamlit as st

# ---------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------
st.set_page_config(
    page_title="Bautizo de Mi Bebé 💖",
    page_icon="👶",
    layout="centered",
)

# ---------------------------
# ESTILOS PERSONALIZADOS
# ---------------------------
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 46px;
            color: #6A5ACD;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 22px;
            color: #444;
            margin-bottom: 25px;
            font-style: italic;
        }
        .section {
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
            padding: 25px;
            border-radius: 20px;
            margin-bottom: 25px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            font-size: 15px;
            color: #666;
            margin-top: 40px;
        }
        .maps-link a {
            color: #1E90FF;
            font-weight: bold;
            text-decoration: none;
        }
        .maps-link a:hover {
            text-decoration: underline;
            color: #104E8B;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# TÍTULO Y FOTO PRINCIPAL
# ---------------------------
st.markdown('<p class="title">👶 Bienvenidos al Bautizo</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Un día especial lleno de amor, fe y bendiciones ✨</p>', unsafe_allow_html=True)

# Cambia la imagen por la tuya en GitHub o una URL pública
st.image("foto_bautizo.jpg", use_column_width=True, caption="Nuestro Gran Día 💖")

# ---------------------------
# SECCIONES
# ---------------------------
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("📅 Fecha y Hora")
    st.write("Sabado 11 de Octubre, 01:00 PM")
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("⛪ Lugar de la Ceremonia")
    st.markdown(
        '<div class="maps-link">📍 <a href="https://maps.app.goo.gl/aVP5rF6QRNbWDkFe7" target="_blank">Parroquia Santiago Apóstol Temoaya, Estado de México</a></div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("🎉 Recepción")
    st.markdown(
        '<div class="maps-link">📍 <a href="https://maps.app.goo.gl/33tSss5ciYpMkhnC7" target="_blank">Pescados y Mariscos El Rey Del Mar, Carr Toluca-Temoaya, Fraccionamiento Urbano Buenaventura, 50850 San Diego Alcalá, Méx.</a></div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("💌 Confirmación de Asistencia")
    nombre = st.text_input("✨ Escribe tu nombre:")
    asistencia = st.radio("¿Podrás acompañarnos?", ["Sí 💖", "No 😢"])
    if st.button("✅ Enviar confirmación"):
        if nombre.strip() == "":
            st.warning("Por favor, escribe tu nombre 🙏")
        else:
            st.success(f"🎉 ¡Gracias {nombre}! Hemos registrado tu respuesta: {asistencia}")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# PIE DE PÁGINA
# ---------------------------
st.markdown('<p class="footer">✨ Gracias por acompañarnos en este día tan especial ✨</p>', unsafe_allow_html=True)
