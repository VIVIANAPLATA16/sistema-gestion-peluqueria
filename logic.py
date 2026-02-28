from database import conectar

def registrar_cliente(nombre, telefono):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
    conn.commit()
    conn.close()

def buscar_cliente(nombre):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def editar_cliente(id_cliente, nuevo_nombre, nuevo_telefono):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nombre = ?, telefono = ? WHERE id = ?", (nuevo_nombre, nuevo_telefono, id_cliente))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes
