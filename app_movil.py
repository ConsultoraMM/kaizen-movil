import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import json

# Configuración de página
st.set_page_config(page_title="Kaizen Móvil", page_icon="📈")
st.title("Registro Kaizen Móvil")

# --- CONFIGURACIÓN DE GOOGLE SHEETS ---
# Subirás tu archivo JSON como un "Secret" en la configuración de Streamlit
def get_gspread_client():
    # Esta parte lee los secretos que configuraremos en Streamlit Cloud
    creds_dict = json.loads(st.secrets["gcp_service_account"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, 
            ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
    return gspread.authorize(creds)

# --- INTERFAZ ---
with st.form("registro"):
    descripcion = st.text_input("Concepto / Descripción")
    monto = st.number_input("Monto en Bs", min_value=0.0, format="%.2f")
    tasa = st.number_input("Tasa BCV del día", value=515.18, format="%.2f")
    categoria = st.selectbox("Categoría", ["Ventas", "Comida", "Gastos Operativos", "Insumos Papelería", "Personal / Casa"])
    tipo_registro = st.radio("¿Qué tipo de movimiento es?", ["💰 Ingreso Negocio", "👤 Ingreso Personal", "💸 Gasto / Egreso"])
    
    enviar = st.form_submit_button("Registrar en el Buzón")

if enviar:
    if descripcion == "":
        st.error("Por favor, coloca una descripción.")
    else:
        try:
            # Conexión y guardado
            client = get_gspread_client()
            sheet = client.open("BD_Kaizen_Movil").sheet1
            
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Fila: Fecha | Descripcion | Monto | Tasa | Categoria | Tipo
            fila = [fecha, descripcion, monto, tasa, categoria, tipo_registro]
            
            sheet.append_row(fila)
            st.success(f"¡Registrado con éxito, Morelys! {descripcion} ya está en el buzón.")
        except Exception as e:
            st.error(f"Error al conectar con Google Sheets: {e}")