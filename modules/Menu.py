from modules.Tiquetes import mostrar_tiquetes, comprar_tiquete

usuarios = {}

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Cuenta")
        print("2. Iniciar Sesión")
        print("3. Salir")
        print()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Registro de Usuario ---")
            nombre_usuario = input("Nombre de usuario: ")

            if nombre_usuario in usuarios:
                print("Este usuario ya existe, intenta con otro.")
            else:
                correo = input("Correo: ")
                contraseña_usuario = input("Contraseña: ")

                print("\n¿Qué eres?")
                print("1. Cliente")
                print("2. Revendedor")
                tipo = input("Elige una opción: ")

                if tipo == "1":
                    tipo_usuario = "Cliente"
                elif tipo == "2":
                    tipo_usuario = "Revendedor"
                else:
                    print("Opción inválida, se asignará como Cliente.")
                    tipo_usuario = "Cliente"

                usuarios[nombre_usuario] = {
                    "correo": correo,
                    "contraseña": contraseña_usuario,
                    "tipo": tipo_usuario
                }
                print(f"Usuario {nombre_usuario} creado con éxito.")

        elif opcion == "2":
            print("\n--- Iniciar Sesión ---")
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")

            if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
                print(f"\nBienvenido {usuario} ({usuarios[usuario]['tipo']})")

                if usuarios[usuario]["tipo"] == "Revendedor":
                    menu_revendedor(usuario)
                else:
                    menu_cliente(usuario)

            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente de nuevo.")


def menu_revendedor(usuario):
    while True:
        print(f"\n--- Sistema de Boletos (Revendedor: {usuario}) ---")
        print("1. Vender un boleto")
        print("2. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Aquí irá la lógica de vender boleto (otra rama).")
        elif opcion == "2":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


def menu_cliente(usuario):
    while True:
        print(f"\n--- Sistema de Boletos (Cliente: {usuario}) ---")
        print("1. Ver boletos disponibles")
        print("2. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tiquetes()  # función conectada con Tiquetes.py
        elif opcion == "2":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    menu_principal()
