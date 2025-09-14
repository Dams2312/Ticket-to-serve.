from Menu.tiquetes import Tiquete, mostrar_tiquetes, comprar_tiquete

usuarios = {}

while True:
    print("\n--- Sistema de Boletos ---")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Registro de Usuario ---")
        nombre_usuario = input("Nombre de usuario: ")

        if nombre_usuario in usuarios:
            print("Ese usuario ya existe. Intente con otro.")
            continue

        correo = input("Correo: ")
        contraseña = input("Contraseña: ")

        print("Seleccione tipo de usuario:")
        print("1. Cliente")
        print("2. Revendedor")
        tipo = input("Opción: ")

        if tipo == "1":
            tipo_usuario = "cliente"
        elif tipo == "2":
            tipo_usuario = "revendedor"
        else:
            print("Opción no válida.")
            continue

        usuarios[nombre_usuario] = {
            "correo": correo,
            "contraseña": contraseña,
            "tipo": tipo_usuario
        }
        print(f"Usuario {nombre_usuario} creado con éxito.\n")

    elif opcion == "2":
        print("\n--- Inicio de Sesión ---")
        nombre_usuario = input("Nombre de usuario: ")
        contraseña = input("Contraseña: ")

        if nombre_usuario in usuarios and usuarios[nombre_usuario]["contraseña"] == contraseña:
            print(f"\nInicio de sesión exitoso. Bienvenido {nombre_usuario}.\n")
            tipo = usuarios[nombre_usuario]["tipo"]

            if tipo == "cliente":
                while True:
                    print(f"\n--- Menú Cliente ({nombre_usuario}) ---")
                    print("1. Ver boletos disponibles")
                    print("2. Cerrar sesión")
                    op = input("Seleccione una opción: ")

                    if op == "1":
                        mostrar_tiquetes()
                    elif op == "2":
                        print("Sesión cerrada.\n")
                        break
                    else:
                        print("Opción no válida.\n")

            elif tipo == "revendedor":
                while True:
                    print(f"\n--- Menú Revendedor ({nombre_usuario}) ---")
                    print("1. Vender un boleto")
                    print("2. Cerrar sesión")
                    op = input("Seleccione una opción: ")

                    if op == "1":
                        comprar_tiquete()
                    elif op == "2":
                        print("Sesión cerrada.\n")
                        break
                    else:
                        print("Opción no válida.\n")

        else:
            print("Usuario o contraseña incorrectos.\n")

    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.\n")