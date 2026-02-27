import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("peluqueria.db")
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servicios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()
    print("Base de datos creada correctamente.")

if __name__ == "__main__":
    crear_base_datos()
