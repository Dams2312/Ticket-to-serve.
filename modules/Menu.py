from modules.Tiquetes import crear_tiquete, obtener_tiquetes_disponibles

usuarios = {}

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Cuenta")
        print("2. Iniciar Sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Registro de Usuario ---")
            nombre_usuario = input("Nombre de usuario: ")

            if nombre_usuario in usuarios:
                print("Este usuario ya existe, intenta con otro.")
            else:
                correo = input("Correo: ")
                contraseña_usuario = input("Contraseña: ")
                usuarios[nombre_usuario] = {
                    "correo": correo,
                    "contraseña": contraseña_usuario
                }
                print("Usuario registrado con éxito.")

        elif opcion == "2":
            nombre_usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")

            if nombre_usuario in usuarios and usuarios[nombre_usuario]["contraseña"] == contraseña:
                print(f"\nBienvenido {nombre_usuario}")
                menu_usuario()
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


def menu_usuario():
    while True:
        print("\n¿Quién eres?")
        print("1. Revendedor")
        print("2. Cliente")
        print("3. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_revendedor()
        elif opcion == "2":
            menu_cliente()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")


def menu_revendedor():
    while True:
        print("\n--- Menú Revendedor ---")
        print("1. Vender tiquete")
        print("2. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID del tiquete: ")
            nombre = input("Nombre del evento: ")
            precio = float(input("Precio: "))
            clase = input("Clase del tiquete (económica/premium/primera clase - opcional): ")
            if clase.strip() == "":
                clase = None
            crear_tiquete(id, nombre, precio, clase)
            print("Tiquete puesto en venta.")

        elif opcion == "2":
            break
        else:
            print("Opción inválida.")


def menu_cliente():
    print("\n--- Tiquetes disponibles ---")
    tiquetes = obtener_tiquetes_disponibles()
    if not tiquetes:
        print("No hay tiquetes disponibles.")
    else:
        for t in tiquetes:
            clase = f" - {t.clase}" if t.clase else ""
            print(f"Tiquete {t.id} - {t.nombre_evento} - ${t.precio}{clase}")


if __name__ == "__main__":
    menu_principal()
