import streamlit as st
import pandas as pd
import datetime

# 1. Configuración Pro
st.set_page_config(page_title="GlamCode Pro", layout="wide")

# 2. CSS de Alto Nivel (Minimalismo Luxury)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #050505; /* Negro absoluto */
        font-family: 'Inter', sans-serif;
    }
    
    .stHeader { background: transparent; }

    /* Tarjetas de cristal (Glassmorphism) */
    .css-1r6p8d1, .stDataFrame {
        border: 1px solid #1A1A1A;
        border-radius: 15px;
        background: #0A0A0A;
    }

    /* Botón con degradado */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%);
        color: black !important;
        border: none;
        padding: 15px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 8px;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.3);
    }

    h1 { color: #FFFFFF; font-weight: 700; letter-spacing: -1px; }
    h3 { color: #D4AF37; font-weight: 300; }
    
    /* Input styling */
    input { background-color: #111 !important; border-color: #333 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Interfaz
st.markdown("<h1 style='text-align: left; font-size: 3rem;'>GlamCode <span style='color:#D4AF37'>OS</span></h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.markdown("### ⚡ NUEVO SERVICIO")
    with st.form("registro_lujo"):
        nombre = st.text_input("NOMBRE DEL CLIENTE", placeholder="Ej. Viviana Plata")
        servicio = st.selectbox("CATEGORÍA", ["Corte Boutique", "Colorimetría Pro", "Tratamiento Diamond"])
        valor = st.number_input("VALOR ($)", min_value=0, step=10000)
        enviar = st.form_submit_button("REGISTRAR EN SISTEMA")
        
        if enviar:
            st.toast("Guardado en la nube", icon="☁️")

with col2:
    st.markdown("### 📋 AGENDA DE HOY")
    # Datos limpios
    df = pd.DataFrame({
        "Hora": ["10:00 AM", "11:30 AM", "02:00 PM"],
        "Cliente": ["Viviana Plata", "Marta Gomez", "Carlos Ruiz"],
        "Estado": ["✅ Confirmado", "⌛ Pendiente", "✅ Confirmado"]
    })
    st.table(df)

st.sidebar.markdown("---")
st.sidebar.caption("SaaS para Peluquerías de Autor v.2.0")
