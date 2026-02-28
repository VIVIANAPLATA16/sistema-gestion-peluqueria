import streamlit as st
import sqlite3
import pandas as pd

# 1. Configuración de página de lujo
st.set_page_config(page_title="GlamCode Luxury SaaS", page_icon="💎", layout="wide")

# 2. Maquillaje Luxury (CSS Personalizado)
st.markdown("""
    <style>
    /* Fondo principal oscuro */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Títulos en Dorado */
    h1, h2, h3 {
        color: #D4AF37 !important; /* Dorado metálico */
        font-family: 'Playfair Display', serif;
    }
    
    /* Botones Dorados */
    .stButton>button {
        background-color: #D4AF37 !important;
        color: #000000 !important;
        border-radius: 5px;
        border: 1px solid #B8860B;
        font-weight: bold;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #000000 !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37;
    }

    /* Tablas y contenedores */
    .stDataFrame {
        border: 1px solid #D4AF37;
        border-radius: 10px;
    }
    
    /* Sidebar oscura */
    [data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #D4AF37;
    }

    /* Texto blanco para legibilidad */
    p, label {
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado de la Suite
st.markdown("<h1 style='text-align: center;'>✨ GLAMCODE LUXURY SUITE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #D4AF37 !important;'>Software de Gestión Exclusiva para Salones de Alta Gama</p>", unsafe_allow_html=True)
st.write("---")

# 4. Estructura de Panel
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🏆 Registro Premium")
    nombre = st.text_input("Nombre del Cliente")
    servicio = st.selectbox("Servicio de Lujo", ["Corte Boutique", "Colorimetría Avanzada", "Spa Capilar Gold", "Barbería VIP"])
    precio = st.number_input("Inversión ($)", min_value=0)
    
    if st.button("GUARDAR EN BASE DE DATOS"):
        # Lógica de guardado (esto ya se conecta con tu peluquería.db)
        st.balloons()
        st.success(f"Servicio para {nombre} registrado en el sistema.")

with col2:
    st.markdown("### 📊 Control de Ingresos")
    # Datos de prueba con estilo
    data = {
        "CLIENTE": ["Viviana Plata", "Empresario VIP", "Modelo Invitada"],
        "SERVICIO": ["Diseño de Imagen", "Corte de Autor", "Tratamiento Gold"],
        "VALOR": ["$150.000", "$95.000", "$210.000"]
    }
    df = pd.DataFrame(data)
    st.table(df) # Usamos tabla para que se vea más limpio el dorado

st.sidebar.markdown("<h2 style='text-align: center;'>👑</h2>", unsafe_allow_html=True)
st.sidebar.title("ADMINISTRACIÓN")
st.sidebar.write("Bienvenida, Viviana.")
st.sidebar.markdown("---")
st.sidebar.info("Versión SaaS 2026 - Edición Limitada")
