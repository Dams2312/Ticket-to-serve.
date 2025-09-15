class Tiquete:
    def __init__(self, id, nombre_evento, precio, clase=None, disponible=True):
        self.id = id
        self.nombre_evento = nombre_evento
        self.precio = precio
        self.clase = clase
        self.disponible = disponible

    def __repr__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        clase_str = f" - {self.clase}" if self.clase else ""
        return f"<Tiquete {self.id} - {self.nombre_evento} - ${self.precio}{clase_str} - {estado}>"


TIQUETES = []

def crear_tiquete(id, nombre_evento, precio, clase=None):
    tiquete = Tiquete(id, nombre_evento, precio, clase)
    TIQUETES.append(tiquete)
    return tiquete

def cambiar_disponibilidad(id, disponible):
    for t in TIQUETES:
        if t.id == id:
            t.disponible = disponible
            return True
    return False

def obtener_tiquetes_disponibles():
    return [t for t in TIQUETES if t.disponible]
