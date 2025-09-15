# modules/Tiquetes.py
# Módulo para manejar la lógica de tiquetes
TIQUETES = []

def crear_tiquete(id, nombre_evento, precio):
    tiquete = {
        "id":id,
        "nombre_evento":nombre_evento,
        "precio" : precio,
        "disponible": True
    }
    TIQUETES.append(tiquete)
    return tiquete

def cambiar_disponibilidad(id, disponible):
    for t in TIQUETES:
        if t["id"] == id:
            t["disponible"] = disponible
            return True
    return False

def obtener_tiquetes_disponibles():
    return [t for t in TIQUETES if t["disponible"]]

def mostrar_tiquete(t):
    estado = "Disponible" if t["disponible"] else "No disponible"
    return f"<Tiquete {t['id']} - {t['nombre_evento']} - ${t['precio']} - {estado}>"

def menu_revendedor():
    while True:
        print("\nOpciones Revendedor:")
        print("1. Crear tiquete")
        print("2. Cambiar disponibilidad de tiquete")
        print("3. Mostrar tiquetes disponibles")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            id = input("ID del tiquete: ")
            nombre = input("Nombre del evento: ")
            precio = float(input("Precio: "))
            crear_tiquete(id, nombre, precio)
            print("Tiquete creado.")

        elif opcion == "2":
            id = input("ID del tiquete a cambiar disponibilidad: ")
            disponible = input("Disponible? (s/n): ").lower() == "s"
            if cambiar_disponibilidad(id, disponible):
                print("Disponibilidad actualizada.")
            else:
                print("Tiquete no encontrado.")

        elif opcion == "3":
            tiquetes = obtener_tiquetes_disponibles()
            print("\nTiquetes disponibles:")
            for t in tiquetes:
                print(t)

        elif opcion == "4":
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

def menu_cliente():
    print("\n--- Tiquetes disponibles para el cliente ---")
    tiquetes = obtener_tiquetes_disponibles()
    if not tiquetes:
        print("No hay tiquetes disponibles.")
    else:
        for t in tiquetes:
            print(f"Tiquete {t['id']} - {t['nombre_evento']} - Disponible")

