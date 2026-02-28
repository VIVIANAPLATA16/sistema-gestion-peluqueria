import streamlit as st
import pandas as pd

st.set_page_config(page_title="GlamCode OS", page_icon="💎", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #050505 !important; }
.main-title {
background: linear-gradient(90deg, #D4AF37, #F9E79F);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
font-size: 3.5rem; font-weight: 700; text-align: center;
}
.card {
background: rgba(255, 255, 255, 0.02);
border: 1px solid rgba(212, 175, 55, 0.15);
border-radius: 20px; padding: 25px; text-align: center;
}
.stButton>button {
width: 100%; background: linear-gradient(90deg, #D4AF37, #B8860B) !important;
color: black !important; border-radius: 50px !important; font-weight: 700;
}
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">GLAMCODE OS</h1>', unsafe_allow_html=True)
st.write("---")

m1, m2, m3 = st.columns(3)
with m1:
st.markdown('<div class="card"><p style="color:#D4AF37;">INGRESOS</p><h2 style="color:white;">$ 1.250.000</h2></div>', unsafe_allow_html=True)
with m2:
st.markdown('<div class="card"><p style="color:#D4AF37;">CITAS</p><h2 style="color:white;">14</h2></div>', unsafe_allow_html=True)
with m3:
st.markdown('<div class="card"><p style="color:#D4AF37;">SISTEMA</p><h2 style="color:white;">ONLINE ✨</h2></div>', unsafe_allow_html=True)

st.write("---")

col_f, col_t = st.columns([1, 1.8], gap="large")

with col_f:
st.markdown("<h3 style='color:#D4AF37;'>🖋️ REGISTRO VIP</h3>", unsafe_allow_html=True)
nombre = st.text_input("NOMBRE")
servicio = st.selectbox("SERVICIO", ["Corte Boutique", "Balayage Diamond", "Seda Capilar"])
if st.button("CONFIRMAR"):
st.balloons()

with col_t:
st.markdown("<h3 style='color:#D4AF37;'>📋 AGENDA HOY</h3>", unsafe_allow_html=True)
datos = {"CLIENTE": ["Viviana Plata", "Carolina Herrera"], "SERVICIO": ["Corte", "Color"]}
st.table(pd.DataFrame(datos))
