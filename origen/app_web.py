import streamlit as st
import sqlite3
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Sistema Gestión Peluquería Pro", page_icon="✂️")

st.title("✂️ Software de Gestión para Peluquerías")
st.subheader("Panel de Administración - Control de Clientes")

# Función para conectar a la base de datos
def obtener_datos():
    conexion = sqlite3.connect('datos/peluqueria.db')
    df = pd.read_sql_query("SELECT * FROM clientes", conexion)
    conexion.close()
    return df

# Interfaz lateral para agregar datos
st.sidebar.header("Registrar Nuevo Servicio")
nombre = st.sidebar.text_input("Nombre del Cliente")
servicio = st.sidebar.selectbox("Servicio", ["Corte Caballero", "Corte Dama", "Barba", "Tintura", "Manicura"])
precio = st.sidebar.number_input("Precio ($)", min_value=0)

if st.sidebar.button("Guardar Registro"):
    conexion = sqlite3.connect('datos/peluqueria.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (nombre, servicio, precio) VALUES (?, ?, ?)", (nombre, servicio, precio))
    conexion.commit()
    conexion.close()
    st.sidebar.success("✅ Registro guardado con éxito")

# Mostrar la tabla de datos real
st.write("### Listado de Servicios Actuales")
try:
    datos = obtener_datos()
    st.table(datos)
except:
    st.warning("La base de datos está vacía o se está inicializando...")

st.info("Desarrollado por Viviana Plata | Software Escala 2026")
