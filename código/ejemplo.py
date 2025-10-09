# Importamos datetime para obtener la hora actual
from datetime import datetime 

def saludar(nombre):
    # Obtenemos la hora actual 
    hora = datetime.now().strftime("%H:%M")  
    return f"Hola {nombre}, son las {hora}. Bienvenido al ejemplo de Python"

if __name__ == "__main__":
    print(saludar("Equipo verde"))
