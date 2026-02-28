import sqlite3

def conectar():
    return sqlite3.connect("peluqueria.db")

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    # Tabla clientes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL
    )
    """)

    # Tabla servicios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servicios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
    """)

    # Tabla citas (relaciona cliente y servicio)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        servicio_id INTEGER,
        fecha TEXT,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id),
        FOREIGN KEY (servicio_id) REFERENCES servicios(id)
    )
    """)

    conexion.commit()
    conexion.close()

# ---------------- CLIENTES ----------------

def agregar_cliente():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
    conexion.commit()
    conexion.close()
    print("Cliente agregado.")

def listar_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    for cliente in cursor.fetchall():
        print(cliente)
    conexion.close()

# ---------------- SERVICIOS ----------------

def agregar_servicio():
    nombre = input("Nombre del servicio: ")
    precio = float(input("Precio: "))

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO servicios (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conexion.commit()
    conexion.close()
    print("Servicio agregado.")

def listar_servicios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM servicios")
    for servicio in cursor.fetchall():
        print(servicio)
    conexion.close()

# ---------------- CITAS ----------------

def agendar_cita():
    cliente_id = int(input("ID del cliente: "))
    servicio_id = int(input("ID del servicio: "))
    fecha = input("Fecha (YYYY-MM-DD): ")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO citas (cliente_id, servicio_id, fecha) VALUES (?, ?, ?)",
                   (cliente_id, servicio_id, fecha))
    conexion.commit()
    conexion.close()
    print("Cita agendada.")

def listar_citas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT citas.id, clientes.nombre, servicios.nombre, citas.fecha
        FROM citas
        JOIN clientes ON citas.cliente_id = clientes.id
        JOIN servicios ON citas.servicio_id = servicios.id
    """)
    for cita in cursor.fetchall():
        print(cita)
    conexion.close()

# ---------------- MENÚ ----------------

def menu():
    while True:
        print("\n--- SISTEMA PELUQUERÍA ---")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Agregar servicio")
        print("4. Listar servicios")
        print("5. Agendar cita")
        print("6. Listar citas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            agregar_servicio()
        elif opcion == "4":
            listar_servicios()
        elif opcion == "5":
            agendar_cita()
        elif opcion == "6":
            listar_citas()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    crear_tablas()
    menu()
