import sqlite3

def conectar():
    return sqlite3.connect("peluqueria.db")

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()

def agregar_cliente():
    nombre = input("Ingrese nombre del cliente: ")
    telefono = input("Ingrese teléfono: ")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
    conexion.commit()
    conexion.close()

    print("Cliente agregado correctamente.")

def listar_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

    conexion.close()

def menu():
    while True:
        print("\n--- SISTEMA PELUQUERÍA ---")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    crear_tablas()
    menu()
