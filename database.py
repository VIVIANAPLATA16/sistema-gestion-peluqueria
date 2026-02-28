import sqlite3
def conectar():
    return sqlite3.connect("peluqueria.db")
def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, telefono TEXT)")
    conn.commit()
    conn.close()
