import os
import json
from typing import Dict
import modules.Tiquetes as Ti
import modules.datos as dat

sincron = "data/comprador.json"
sincro = "data/vendedor.json"

def menu_principal():
    print("""
        --------------------------------------
        --- Sistema de Gestión de Tiquetes ---
        --------------------------------------
        1. Registrarse
        2. Iniciar sesión
        3. Salir
        ---------------------------------------
    """, end="")
    opcion = input("Seleccione una opción: ")
    return opcion

def registro(usuarios):
    usuarios.update(dat.leer_compras(sincron))
    usuarios.update(dat.leer_compras(sincro))

    while True:
        try:
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
            
            if tipo_usuario == "cliente":
                dat.escribir_compra(sincron, usuarios)
                input("Registro exitoso. Presione ENTER para continuar e iniciar sesión...")
            else:
                dat.escribir_compra(sincro, usuarios)
                input("Registro exitoso. Presione ENTER para continuar e iniciar sesión...")

            print(f"\nUsuario {nombre_usuario} registrado exitosamente como {tipo_usuario}.\n")
            return "2"
        except ValueError:
            print("Error en el registro. Intente de nuevo.\n")
        except KeyError:
            print("Error en el registro. Intente de nuevo.\n")
        except Exception as e:
            print("Error inesperado. Intente de nuevo.\n")
            print(f"Error inesperado: {e}")

def sesion(usuarios: Dict):
    while True:
        try:
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
                        print("2. Ver mis boletos")
                        print("3. Cerrar sesión")
                        op = input("Seleccione una opción: ")

                        if op == "1":
                            Ti.menu_cliente()
                        elif op == "2":
                            Ti.ver_tiket()
                        elif op == "3":
                            print("Sesión cerrada.\n")
                            return None
                        else:
                            print("Opción no válida.\n")

                elif tipo == "revendedor":
                    while True:
                        print(f"\n--- Menú Revendedor ({nombre_usuario}) ---")
                        print("1. Vender un boleto")
                        print("2. Cerrar sesión")
                        op = input("Seleccione una opción: ")

                        if op == "1":
                            Ti.menu_revendedor()
                        elif op == "2":
                            print("Sesión cerrada.\n")
                            return None
                        else:
                            print("Opción no válida.\n")

                else:
                    print("Error al identificar tipo de usuario.\n")
            else:
                print("Usuario o contraseña incorrectos.\n")
        except KeyError:            
            print("Error en el inicio de sesión. Intente de nuevo.\n")
        except Exception as e:
            print("Error inesperado. Intente de nuevo.\n")
            print(f"Error inesperado: {e}")
