import sqlite3

def conectar():
    """Establece la conexión con la base de datos."""
    return sqlite3.connect("peluqueria.db")

def crear_tablas():
    """Crea las tablas si no existen."""
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        telefono TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS servicios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        precio REAL NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS citas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cliente_id INTEGER,
                        servicio_id INTEGER,
                        fecha TEXT,
                        FOREIGN KEY(cliente_id) REFERENCES clientes(id),
                        FOREIGN KEY(servicio_id) REFERENCES servicios(id))''')
    
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()
    print("Base de datos e infraestructura lista.")
