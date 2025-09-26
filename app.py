import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Invitación al Bautizo",
    page_icon="👶",
    layout="centered"
)

# Encabezado
st.title("👶✨ Invitación Especial ✨👶")
st.subheader("¡Con mucha alegría queremos invitarte al bautizo de nuestro(a) pequeñ@!")

# Imagen (puedes cambiar la URL por la tuya o subir una imagen a la carpeta)
st.image(
    "https://i.ibb.co/ydqM1sP/bautizo.jpg",
    caption="Nuestro(a) angelito está por recibir el bautizo 💕",
    use_column_width=True
)

# Información principal
st.markdown(
    """
    ### 📅 Fecha y hora  
    **Sabado, 11 de Octubre de 2025 - 12:00 p.m.**

    ### ⛪ Ceremonia  
    Parroquia Temoaya Estado de México  

    ### 🎉 Recepción  
    Pescados y Mariscos El Rey Del Mar 
    """
)

# Mensaje especial
st.success("Será un día muy especial y nos encantará contar con tu presencia 🙏✨")

# Sección de confirmación
st.markdown("## 📩 Confirmar Asistencia")

with st.form("confirmar_form"):
    nombre = st.text_input("Tu nombre")
    acompanantes = st.number_input("Número de acompañantes", min_value=0, max_value=10, step=1)
    mensaje = st.text_area("Mensaje para la familia")
    confirmar = st.form_submit_button("Confirmar asistencia")

    if confirmar:
        if nombre:
            st.success(f"🎉 ¡Gracias {nombre}! Hemos registrado tu asistencia con {acompanantes} acompañante(s).")
        else:
            st.error("Por favor, escribe tu nombre antes de confirmar.")

# Mapa de ubicación (con Google Maps embebido)
st.markdown("## 📍 Cómo llegar")
st.components.v1.iframe(
    "https://maps.app.goo.gl/KAQH8bBxNaNGGsAu5",
    height=400
)

# Mensaje final
st.markdown(
    """
    ---
    ❤️ Con cariño,  
    **Familia Bermudez Bermudez**
    """
)
