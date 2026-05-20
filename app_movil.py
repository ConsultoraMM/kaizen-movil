import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Kaizen Móvil", page_icon="📈")
st.title("Registro Kaizen")

# Formulario simple para el móvil
with st.form("registro"):
    descripcion = st.text_input("Descripción")
    monto = st.number_input("Monto en Bs", min_value=0.0)
    categoria = st.selectbox("Categoría", ["Operación", "Inversión", "Personal"])
    enviar = st.form_submit_button("Registrar")

if enviar:
    # Aquí es donde el dato llega a la "nube" (Google Sheets o una base simple)
    # Por ahora, simularemos el registro
    st.success(f"Registrado: {descripcion} - {monto} Bs")
    # En el siguiente paso conectaremos esto a tu buzón seguro