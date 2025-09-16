import json

def escribir_compra(file_path : str ,data : dict ) -> None:

    try: 
        with open(file_path, 'w', encoding='utf-8') as Compras:
            json.dump(data, Compras , indent=4)


    except IOError as Error :
        print (f"erro al escribir en  el archivo {file_path}: {Error}")



def leer_compras(file_path : str) -> dict:
    try:
        with open(file_path, 'r', encoding='utf-8') as Compras:
            return json.load(Compras)
    except FileNotFoundError:
        return {}
    
