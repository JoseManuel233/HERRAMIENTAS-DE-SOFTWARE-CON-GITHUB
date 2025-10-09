# Importamos datetime para obtener la hora actual
from datetime import datetime 

def saludar(nombre):
    def despedir(nombre):
    return f"Adiós {nombre}, ¡nos vemos pronto!"

def motivar(nombre):
    return f"¡Vamos {nombre}, tú puedes lograrlo!"

    # Obtenemos la hora actual 
    hora = datetime.now().strftime("%H:%M")  
    return f"Hola {nombre}, son las {hora}. Bienvenido al ejemplo de Python"

if __name__ == "__main__":
    print(despedir("Maestra Sydney"))
    print(motivar("Equipo Verde"))
    print(saludar("Equipo verde"))
