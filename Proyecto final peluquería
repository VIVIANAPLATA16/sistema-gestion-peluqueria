import sqlite3
import os
from datetime import datetime

# ==========================================================
# CONFIGURACIÓN Y CONEXIÓN
# ==========================================================

def conectar():
    """Establece la conexión con la base de datos SQLite."""
    return sqlite3.connect("peluqueria.db")

def limpiar_pantalla():
    """Limpia la terminal para mantener una interfaz ordenada."""
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_tablas():
    """Crea las tablas necesarias si no existen."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, telefono TEXT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS servicios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, precio REAL NOT NULL)")
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

# ==========================================================
# MÓDULO DE CLIENTES
# ==========================================================

def agregar_cliente():
    print("\n--- REGISTRO DE NUEVO CLIENTE ---")
    while True:
        nombre = input("Nombre completo: ").strip()
        if len(nombre) >= 3 and not nombre.isdigit(): break
        print("❌ Error: Nombre inválido.")
    while True:
        telefono = input("Teléfono (10 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 10: break
        print("❌ Error: El teléfono debe tener 10 dígitos.")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
    conexion.commit()
    conexion.close()
    print(f"✅ Cliente '{nombre}' guardado.")
    input("\nPresione ENTER para continuar...")

def listar_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    if not clientes:
        print("\n📭 No hay clientes registrados.")
    else:
        print("\n=== LISTADO DE CLIENTES ===")
        for c in clientes:
            print(f"ID: {c[0]} | Nombre: {c[1]} | Teléfono: {c[2]}")
            print("-" * 30)
    input("\nPresione ENTER para continuar...")
    conexion.close()

def eliminar_cliente():
    listar_clientes()
    id_borrar = input("\n🔢 Ingrese el ID del cliente a eliminar (o Enter para cancelar): ")
    if not id_borrar: return
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_borrar,))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f"🗑️ Cliente con ID {id_borrar} eliminado.")
    else:
        print("⚠️ ID no encontrado.")
    conexion.close()
    input("\nPresione ENTER para continuar...")

# ==========================================================
# MÓDULO DE SERVICIOS
# ==========================================================

def agregar_servicio():
    nombre = input("Nombre del servicio: ").strip()
    while True:
        try:
            precio = float(input("Precio: "))
            break
        except ValueError: print("❌ Error: Ingrese números.")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO servicios (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conexion.commit()
    conexion.close()
    print(f"✅ Servicio '{nombre}' agregado.")
    input("\nPresione ENTER para continuar...")

def listar_servicios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM servicios")
    servicios = cursor.fetchall()
    if not servicios:
        print("\n📭 No hay servicios.")
    else:
        print("\n=== LISTADO DE SERVICIOS ===")
        for s in servicios:
            print(f"ID: {s[0]} | Servicio: {s[1]} | Precio: ${s[2]:,.0f}")
            print("-" * 30)
    input("\nPresione ENTER para continuar...")
    conexion.close()

# ==========================================================
# MÓDULO DE CITAS
# ==========================================================

def agendar_cita():
    listar_clientes()
    while True:
        cliente_id = input("🔢 Ingrese el NÚMERO (ID) del cliente: ").strip()
        if cliente_id.isdigit(): break
        print("❌ Ingrese solo el número.")
    
    listar_servicios()
    while True:
        servicio_id = input("🔢 Ingrese el NÚMERO (ID) del servicio: ").strip()
        if servicio_id.isdigit(): break
        print("❌ Ingrese solo el número.")
    
    while True:
        fecha_input = input("📅 Fecha (AAAA-MM-DD): ")
        try:
            datetime.strptime(fecha_input, '%Y-%m-%d')
            fecha = fecha_input
            break
        except ValueError: print("❌ Formato inválido.")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM clientes WHERE id = ?", (cliente_id,))
    existe_c = cursor.fetchone()
    cursor.execute("SELECT id FROM servicios WHERE id = ?", (servicio_id,))
    existe_s = cursor.fetchone()

    if existe_c and existe_s:
        cursor.execute("INSERT INTO citas (cliente_id, servicio_id, fecha) VALUES (?, ?, ?)", (cliente_id, servicio_id, fecha))
        conexion.commit()
        print("\n✅ ¡Cita agendada con éxito!")
    else:
        print("\n❌ Error: IDs no encontrados.")
    conexion.close()
    input("\nPresione ENTER para continuar...")

def listar_citas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT citas.id, clientes.nombre, servicios.nombre, citas.fecha
        FROM citas
        JOIN clientes ON citas.cliente_id = clientes.id
        JOIN servicios ON citas.servicio_id = servicios.id
    """)
    citas = cursor.fetchall()
    if not citas:
        print("\n📅 No hay citas.")
    else:
        print("\n=== LISTADO DE CITAS ===")
        for cita in citas:
            print(f"Cita #{cita[0]} | Cliente: {cita[1]} | Servicio: {cita[2]} | Fecha: {cita[3]}")
            print("-" * 50)
    input("\nPresione ENTER para continuar...")
    conexion.close()

def eliminar_cita():
    """NUEVA FUNCIÓN: Permite borrar citas específicas."""
    listar_citas()
    id_borrar = input("\n🔢 Ingrese el ID de la CITA que desea borrar: ")
    if not id_borrar: return
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM citas WHERE id = ?", (id_borrar,))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f"🗑️ Cita #{id_borrar} eliminada.")
    else:
        print("⚠️ No se encontró esa cita.")
    conexion.close()
    input("\nPresione ENTER para continuar...")

# ==========================================================
# MENÚ PRINCIPAL
# ==========================================================

def menu():
    while True:
        limpiar_pantalla()
        print("==========================================")
        print("     SISTEMA DE GESTIÓN PELUQUERÍA")
        print("==========================================")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Agregar servicio")
        print("4. Listar servicios")
        print("5. Agendar cita")
        print("6. Listar citas")
        print("7. ELIMINAR CLIENTE 🗑️")
        print("8. ELIMINAR CITA 📅🗑️")
        print("9. Salir")
        print("==========================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1": agregar_cliente()
        elif opcion == "2": listar_clientes()
        elif opcion == "3": agregar_servicio()
        elif opcion == "4": listar_servicios()
        elif opcion == "5": agendar_cita()
        elif opcion == "6": listar_citas()
        elif opcion == "7": eliminar_cliente()
        elif opcion == "8": eliminar_cita()
        elif opcion == "9":
            print("\n✨ Gracias por usar el sistema. \n🚀 Desarrollado por Viviana Plata.")
            break
        else:
            print("❌ Opción inválida.")
            input("Presione ENTER...")

if __name__ == "__main__":
    crear_tablas()
    menu()
