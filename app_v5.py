import streamlit as st
import pandas as pd
import os
import time

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
        /* Fondo animado */
        body {
            background: linear-gradient(-45deg, #f9c5d1, #fbc2eb, #a6c1ee, #d4fc79);
            background-size: 400% 400%;
            animation: gradientBG 12s ease infinite;
            font-family: 'Trebuchet MS', sans-serif;
        }
        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .title {
            text-align: center;
            font-size: 52px;
            color: #fff;
            font-weight: bold;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.2);
        }
        .subtitle {
            text-align: center;
            font-size: 24px;
            color: #f8f8f8;
            margin-bottom: 30px;
            font-style: italic;
        }
        .section {
            background: rgba(255,255,255,0.9);
            padding: 25px;
            border-radius: 25px;
            margin: 20px auto;
            width: 85%;
            box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
            transition: transform 0.3s ease;
        }
        .section:hover {
            transform: scale(1.03);
        }
        .footer {
            text-align: center;
            font-size: 15px;
            color: #fff;
            margin-top: 40px;
        }
        .maps-link a {
            color: #ff4081;
            font-weight: bold;
            text-decoration: none;
        }
        .maps-link a:hover {
            text-decoration: underline;
            color: #d81b60;
        }
        /* Imagen circular */
        .circular-img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 50%;
            width: 250px;
            height: 250px;
            object-fit: cover;
            border: 6px solid #fff;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# TÍTULO Y FOTO PRINCIPAL
# ---------------------------
st.markdown('<p class="title">👶 Bienvenidos al Bautizo</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Un día especial lleno de amor, fe y bendiciones ✨</p>', unsafe_allow_html=True)

# FOTO circular del bebé (usar URL pública desde GitHub u otro host)
st.markdown(
    f'<img src="https://raw.githubusercontent.com/tu_usuario/tu_repo/main/foto_bautizo.jpg" class="circular-img" alt="Foto Bautizo">',
    unsafe_allow_html=True
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
            st.balloons()  # 🎈 Efecto de confeti
            time.sleep(1.5)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# PIE DE PÁGINA
# ---------------------------
st.markdown('<p class="footer">✨ Gracias por acompañarnos en este día tan especial ✨</p>', unsafe_allow_html=True)

# ---------------------------
# OPCIONAL: Ver confirmaciones (solo tú)
# ---------------------------
if st.checkbox("🔒 Ver confirmaciones (solo organizadores)"):
    if os.path.exists("confirmaciones.csv"):
        df_confirmaciones = pd.read_csv("confirmaciones.csv")
        st.dataframe(df_confirmaciones)
    else:
        st.info("No hay confirmaciones aún.")
