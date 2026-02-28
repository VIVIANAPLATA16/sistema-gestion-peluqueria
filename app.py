from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = "database.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    # Tabla clientes
    c.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT
        )
    """)
    # Tabla servicios
    c.execute("""
        CREATE TABLE IF NOT EXISTS servicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL
        )
    """)
    # Tabla citas
    c.execute("""
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            servicio_id INTEGER,
            fecha TEXT,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id),
            FOREIGN KEY(servicio_id) REFERENCES servicios(id)
        )
    """)
    conn.commit()
    conn.close()

# -----------------------------
# Dashboard
# -----------------------------
@app.route('/')
def index():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM clientes")
    total_clientes = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM citas")
    total_citas = c.fetchone()[0]
    conn.close()
    return render_template("index.html", total_clientes=total_clientes, total_citas=total_citas)

# -----------------------------
# Clientes
# -----------------------------
@app.route('/clientes')
def clientes():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM clientes")
    lista_clientes = c.fetchall()
    conn.close()
    return render_template("clientes.html", clientes=lista_clientes)

@app.route('/add_cliente', methods=['POST'])
def add_cliente():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO clientes (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
    conn.commit()
    conn.close()
    return redirect(url_for('clientes'))

@app.route('/delete_cliente/<int:id>')
def delete_cliente(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('clientes'))

# -----------------------------
# Servicios
# -----------------------------
@app.route('/servicios')
def servicios():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM servicios")
    lista_servicios = c.fetchall()
    conn.close()
    return render_template("servicios.html", servicios=lista_servicios)

@app.route('/add_servicio', methods=['POST'])
def add_servicio():
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO servicios (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conn.commit()
    conn.close()
    return redirect(url_for('servicios'))

@app.route('/delete_servicio/<int:id>')
def delete_servicio(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM servicios WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('servicios'))

# -----------------------------
# Citas
# -----------------------------
@app.route('/citas')
def citas():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        SELECT citas.id, clientes.nombre, servicios.nombre, citas.fecha
        FROM citas
        JOIN clientes ON citas.cliente_id = clientes.id
        JOIN servicios ON citas.servicio_id = servicios.id
    """)
    lista_citas = c.fetchall()
    c.execute("SELECT * FROM clientes")
    clientes = c.fetchall()
    c.execute("SELECT * FROM servicios")
    servicios = c.fetchall()
    conn.close()
    return render_template("citas.html", citas=lista_citas, clientes=clientes, servicios=servicios)

@app.route('/add_cita', methods=['POST'])
def add_cita():
    cliente_id = request.form['cliente_id']
    servicio_id = request.form['servicio_id']
    fecha = request.form['fecha']
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO citas (cliente_id, servicio_id, fecha) VALUES (?, ?, ?)",
              (cliente_id, servicio_id, fecha))
    conn.commit()
    conn.close()
    return redirect(url_for('citas'))

@app.route('/delete_cita/<int:id>')
def delete_cita(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM citas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('citas'))

# -----------------------------
# Ejecutar app
# -----------------------------
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
