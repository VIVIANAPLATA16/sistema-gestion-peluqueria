import streamlit as st
import pandas as pd

st.set_page_config(page_title="GlamCode OS", page_icon="", layout="wide")

st.markdown("""
# GLAMCODE OS
""", unsafe_allow_html=True)

st.write("---")

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown("""
    ### INGRESOS
    ## $ 1.250.000
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    ### CITAS
    ## 14
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    ### SISTEMA
    ## ONLINE ✨
    """, unsafe_allow_html=True)

st.write("---")

col_f, col_t = st.columns([1, 1.8], gap="large")

with col_f:
    st.markdown("""
    ### 🔹 REGISTRO VIP
    """, unsafe_allow_html=True)
    nombre = st.text_input("NOMBRE")
    servicio = st.selectbox("SERVICIO", ["Corte Boutique", "Balayage Diamond", "Seda Capilar"])
    if st.button("CONFIRMAR"):
        st.balloons()
        st.success(f"¡Registrado: {nombre} - {servicio}!")

with col_t:
    st.markdown("""
    ### 📅 AGENDA HOY
    """, unsafe_allow_html=True)
    datos = {
        "CLIENTE": ["Viviana Plata", "Carolina Herrera"],
        "SERVICIO": ["Corte", "Color"]
    }
    st.table(pd.DataFrame(datos))
