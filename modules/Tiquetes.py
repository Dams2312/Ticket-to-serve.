# modules/Tiquetes.py
# Módulo para manejar la lógica de tiquetes
import json
from typing import Dict,List
import modules.datos as dat

sesion = "Data\comprador.json"
user = "Data\vendedor.json"

TIQUETES = []

usuarios = {}

def crear_tiquete(id, nombre_evento, precio):
    tiquete = {
        "id":id,
        "nombre_evento":nombre_evento,
        "precio" : precio,
        "disponible": True
    }
    TIQUETES.append(tiquete)
    return usuarios

def cambiar_disponibilidad(id, disponible):
    dat.leer_compras(sesion)
    for t in TIQUETES:
        if t["id"] == id:
            t["disponible"] = disponible
            return True
    dat.escribir_compra(sesion,usuarios)
    return False

def obtener_tiquetes_disponibles():
    return [t for t in TIQUETES if t["disponible"]]

def mostrar_tiquete(t):
    estado = "Disponible" if t["disponible"] else "No disponible"
    return f"<Tiquete {t['id']} - {t['nombre_evento']} - ${t['precio']} - {estado}>"

def filtro():
    filtro = [t for t in TIQUETES if t["disponible"]== True]
    return filtro

def menu_revendedor():
    while True:
        try:
            print("\nOpciones Revendedor:")
            print("1. Crear tiquete")
            print("2. Cambiar disponibilidad de tiquete")
            print("3. Mostrar tiquetes disponibles")
            print("4. Salir")

            opcion = input("Elija una opción: ")

            if opcion == "1":
                dat.leer_compras(user)
                id = input("ID del tiquete: ")
                nombre = input("Nombre del evento: ")
                precio = float(input("Precio: "))
                crear_tiquete(id, nombre, precio)
                dat.escribir_compra(user,usuarios)
                print("Tiquete creado.")


            elif opcion == "2":
                dat.leer_compras(user)
                id = input("ID del tiquete a cambiar disponibilidad: ")
                disponible = input("Disponible? (s/n): ").lower() == "s"
                if cambiar_disponibilidad(id, disponible):
                    print("Disponibilidad actualizada.")
                    dat.escribir_compra(user,usuarios)
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
        except ValueError:
            print("ha ocurrido one herror")
        except Exception as e:
            print("ha ocurrido one herror")
            print(f"Error inesperado: {e}")
            
            
def menu_cliente():
    while True:
        try:
            print("\n--- Tiquetes disponibles para el cliente ---")
            tiquetes = obtener_tiquetes_disponibles()
            if not tiquetes:
                print("No hay tiquetes disponibles.")
            else:
                for t in tiquetes:
                    print(f"Tiquete {t['id']} - {t['nombre_evento']} - Disponible")
                seleccione = input("Seleccione el ID del tiquete que desea comprar.")
                tiquete_seleccionado = next((t for t in tiquetes if t["id"] == seleccione), None)
                if tiquete_seleccionado :
                    
                    cambiar_disponibilidad(seleccione, False)
                    usuarios["Boleto"] = {"id":seleccione, "nombre_evento": tiquete_seleccionado["nombre_evento"], "precio": tiquete_seleccionado["precio"]}
                    dat.escribir_compra(sesion,usuarios)
                    print("Compra exitosa")
                else:
                    print("lo sentimos alquien llego primero...")
                    print ("Te volveremos a mostrar la lista actualizada")
                    print("\n--- Tiquetes disponibles para el cliente ---")
                    print(filtro())
        
        except ValueError:
            print("ha ocurrido one herror")
        except KeyError:
            print("ha ocurrido one herror")
        except Exception as e:
            print("ha ocurrido one herror")
            print(f"Error inesperado: {e}")


def ver_tiket():
    while True:
        try:
            print("mostrando voletos comprados....")
            boletos = "Boleto"
            if boletos in usuarios:
                print(f"Boletos comprados: {usuarios['Boleto']}")
            else:
                print("No has comprado ningún boleto.")
            
        except KeyError:
            print("ha ocurrido un herror.....")
        except Exception as e:
            print("ha ocurrido one herror")
            print(f"Error inesperado: {e}")

