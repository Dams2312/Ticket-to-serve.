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
            os.system("cls")
            opciones = Me.menu_principal()
            if opciones == "":
                nueva_opcion = Me.registro(usuarios)
                if nueva_opcion:
                    opciones = nueva_opcion
            
            match opciones:
                case "1":
                    Me.registro(usuarios)
                case "2":
                    Me.sesion(usuarios)
                case "3":
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print("Error inesperado en el sistema. Intente de nuevo.")
            print(f"Error inesperado: {e}")
            continue
