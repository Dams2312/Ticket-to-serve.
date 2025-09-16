# 🎟️ Ticket to serve

## 👨‍💻 Autor
**Danny Julian Velasco Olarte**,
**Jefferson Andres Amarillo**,
**Brayan Castro**,
**Andres Navas**,
**Karen Afanador**

## 🗓️ Fecha de creación
**Septiembre 2025**

---

## 📝 Descripción General

Este proyecto consiste en un sistema de gestión de tiquetes de eventos. Permite a usuarios registrarse como **clientes** o **revendedores**, iniciar sesión, comprar tiquetes (si son clientes) o crear y administrar tiquetes (si son revendedores).

Está desarrollado en Python puro, con lectura y escritura en archivos `.json` para persistencia de datos. No requiere base de datos ni frameworks externos.

---

## ⚙️ Stack Tecnológico

- 🐍 **Python 3.10+**
- 📄 **JSON** (para almacenar usuarios y tiquetes)

---

## 📁 Estructura del Proyecto

```
/Ticket-to-serve/
│
├── main.py # Archivo principal del sistema
├── README.md # Este archivo con la documentación del proyecto
│
├── datas/ # Carpeta para almacenar los datos persistentes
│ ├── comprador.json # Almacena los datos de los clientes y sus compras
│ └── vendedor.json # Almacena los tiquetes creados por revendedores
│
└── modules/ # Módulos de lógica organizados por funcionalidad
├── Menu.py # Manejo del menú principal, registro y login
├── Tiquetes.py # Lógica de tiquetes (crear, comprar, mostrar)
└── datos.py # Lectura y escritura de archivos JSON
```


---

## 📦 Requerimientos

Este proyecto no necesita librerías externas. Solo debes tener instalado:

- Python 3.10 o superior

---

## ▶️ ¿Cómo se utiliza?

1. **Clona o descarga** este repositorio.
2. Asegúrate de que tienes las siguientes carpetas:
   - `modules/` con los archivos `.py`
   - `datas/` con los archivos `comprador.json` y `vendedor.json` vacíos o inicializados como `{}`

3. Abre la terminal y ejecuta:

```bash
python main.py
El menú te permitirá:

Registrarte como cliente o revendedor

Iniciar sesión según tu tipo de usuario

Comprar tiquetes disponibles o crear nuevos (según el rol)

EJEMPLO

        --------------------------------------
        --- Sistema de Gestión de Tiquetes ---
        --------------------------------------
        1. Registrarse
        2. Iniciar sesión
        3. Salir
        ---------------------------------------
    Seleccione una opción: 2

--- Inicio de Sesión ---
Nombre de usuario: Danny
Contraseña: Dams
Usuario o contraseña incorrectos.

```

**BACKLOG**
[Tablero de Trello](https://trello.com/b/bd0roOTP/venta-de-tichetes)

📌 Notas

- Se recomienda no ejecutar directamente los módulos individuales (como Tiquetes.py). El programa debe iniciarse desde main.py.

- En caso de errores en lectura/escritura de archivos JSON, revisa que los archivos existan y estén bien formateados.

- Si vas a compartir este sistema o migrarlo, asegúrate de incluir la carpeta datas/ con los archivos JSON vacíos.
