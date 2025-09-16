"""
Nombre: Danny Velasco,  
Fecha: 12/09/2025
Descripción: Programa proveedor de  un API de tiquetes (boletos
o tickets) para que cada vendedor de tiquetes lo use en su sistema.
Necesitas proveer diferentes funcionalidades para ayudar a tu cliente a manejar el evento y
vender sus tiquetes
"""

import os
import json
from typing import Dict
import modules.Menu as Me

usuarios = {}

if __name__ == "__main__":
    while True:
        try:
            os.system("clear")  # usa "cls" si es Windows
            opciones = Me.menu_principal()

            match opciones:
                case "1":
                    Me.registro(usuarios)

                case "2":
                    resultado = Me.sesion(usuarios)  # guardo el retorno
                    if resultado is None:
                        print("Error en la sesión. Intente de nuevo.")
                    else:
                        print("Sesión iniciada correctamente.")

                case "3":
                    print("Saliendo del sistema...")
                    break  # <-- IMPORTANTE: rompe el bucle

                case _:
                    print("Opción inválida, intente de nuevo.")

            input("\nPresiona Enter para continuar...")

        except Exception as e:
            print(f"Ocurrió un error: {e}")
            break

