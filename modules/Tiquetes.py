class Tiquete:
    def __init__(self, id, nombre_evento, precio, clase="Económica", disponible=True):
        self.id = id
        self.nombre_evento = nombre_evento
        self.precio = precio
        self.clase = clase
        self.disponible = disponible

    def __repr__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"<Tiquete {self.id} - {self.nombre_evento} - {self.clase} - ${self.precio} - {estado}>"

TIQUETES = []
contador_id = 1  

def crear_tiquete(nombre_evento, precio, clase="Económica"):
    global contador_id
    tiquete = Tiquete(contador_id, nombre_evento, precio, clase)
    TIQUETES.append(tiquete)
    contador_id += 1
    return tiquete

def obtener_tiquetes_disponibles():
    return [t for t in TIQUETES if t.disponible]

def mostrar_tiquetes():
    tiquetes = obtener_tiquetes_disponibles()
    if not tiquetes:
        print("No hay tiquetes disponibles.")
    else:
        print("\n--- Lista de tiquetes disponibles ---")
        for t in tiquetes:
            print(f"ID {t.id} - {t.nombre_evento} - {t.clase} - ${t.precio}")

def vender_tiquete():
    nombre = input("Nombre del tiquete: ")
    precio = float(input("Precio: "))
    clase = input("Clase (Económica, Premium, Primera clase) [opcional]: ")
    if clase.strip() == "":
        clase = "Económica"
    tiquete = crear_tiquete(nombre, precio, clase)
    print(f"Tiquete {tiquete.nombre_evento} agregado con éxito.")

def comprar_tiquete():
    mostrar_tiquetes()
    id = input("Ingrese el ID del tiquete que desea comprar: ")
    for t in TIQUETES:
        if str(t.id) == id and t.disponible:
            t.disponible = False
            print(f"Compra realizada del tiquete {t.nombre_evento}.")
            return
    print("Tiquete no disponible o no encontrado.")
