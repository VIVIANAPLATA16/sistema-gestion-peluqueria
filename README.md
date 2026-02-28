# 💇‍♀️ Sistema de Gestión para Peluquería

Proyecto desarrollado como parte de mi formación en Análisis y Desarrollo de Software (ADSO) – SENA.

## 📌 Descripción
Aplicación orientada a la gestión de clientes, servicios y citas para una peluquería, permitiendo organizar la información y mejorar el control administrativo.

## 🚀 Funcionalidades
- Registro de clientes
- Gestión de servicios
- Control de citas
- Base de datos relacional

## 🛠 Tecnologías utilizadas
- Python
- SQLite
- Git
  ## 🗄 Modelo de Base de Datos

El sistema utiliza una base de datos relacional en SQLite con las siguientes tablas:

- **clientes** (id, nombre, telefono)
- **servicios** (id, nombre, precio)
- **citas** (id, cliente_id, servicio_id, fecha)

Las tablas están relacionadas mediante llaves foráneas para garantizar integridad de datos.

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Ejecutar el archivo principal:

```bash
python main.py

## 👩‍💻 Autora
Viviana Plata  
Tecnólogo en Análisis y Desarrollo de Software – SENA
