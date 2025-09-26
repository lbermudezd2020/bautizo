import streamlit as st
import pandas as pd
import os

# ---------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------
st.set_page_config(
    page_title="Bautizo de Mi Bebé 💖",
    page_icon="👶",
    layout="wide",
)

# ---------------------------
# ESTILOS PERSONALIZADOS
# ---------------------------
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom right, #fff0f5, #e6f7ff);
        }
        .title {
            text-align: center;
            font-size: 50px;
            color: #FF69B4;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 24px;
            color: #555;
            margin-bottom: 40px;
            font-style: italic;
        }
        .section {
            background: linear-gradient(135deg, #ffffff 0%, #ffe6f2 100%);
            padding: 30px;
            border-radius: 25px;
            margin-bottom: 30px;
            box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .section:hover {
            transform: scale(1.02);
            box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
        }
        .footer {
            text-align: center;
            font-size: 16px;
            color: #666;
            margin-top: 50px;
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

# FOTO PRINCIPAL (usar URL pública desde GitHub)
st.image(
    "https://raw.githubusercontent.com/tu_usuario/tu_repositorio/main/foto_bautizo.jpg",
    use_container_width=True,
    caption="Nuestro Gran Día 💖"
)

# ---------------------------
# SECCIONES
# ---------------------------
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("📅 Fecha y Hora")
    st.write("Sábado 11 de Octubre, 01:00 PM")
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
        '<div class="maps-link">📍 <a href="https://maps.app.goo.gl/33tSss5ciYpMkhnC7" target="_blank">Pescados y Mariscos El Rey Del Mar, Toluca-Temoaya, Méx.</a></div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# CONFIRMACIÓN DE ASISTENCIA
# ---------------------------
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("💌 Confirmación de Asistencia")
    nombre = st.text_input("✨ Escribe tu nombre:")
    asistencia = st.radio("¿Podrás acompañarnos?", ["Sí 💖", "No 😢"])
    if st.button("✅ Enviar confirmación"):
        if nombre.strip() == "":
            st.warning("Por favor, escribe tu nombre 🙏")
        else:
            # Guardar en CSV
            data_file = "confirmaciones.csv"
            new_entry = pd.DataFrame({"Nombre":[nombre], "Asistencia":[asistencia]})
            if os.path.exists(data_file):
                df = pd.read_csv(data_file)
                df = pd.concat([df, new_entry], ignore_index=True)
            else:
                df = new_entry
            df.to_csv(data_file, index=False)
            st.success(f"🎉 ¡Gracias {nombre}! Hemos registrado tu respuesta: {asistencia}")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# PIE DE PÁGINA
# ---------------------------
st.markdown('<p class="footer">✨ Gracias por acompañarnos en este día tan especial ✨</p>', unsafe_allow_html=True)

# ---------------------------
# OPCIONAL: Ver confirmaciones (solo tú)
# ---------------------------
if st.checkbox("🔒 Ver confirmaciones (privado)"):
    if os.path.exists("confirmaciones.csv"):
        df_confirmaciones = pd.read_csv("confirmaciones.csv")
        st.dataframe(df_confirmaciones)
    else:
        st.info("No hay confirmaciones aún.")
