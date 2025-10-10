from datetime import datetime

def despedir(nombre):
    return f"Adiós {nombre}, ¡nos vemos pronto!"

def motivar(nombre):
    return f"¡Vamos {nombre}, tú puedes lograrlo!"

def saludar(nombre):
    # Obtenemos la hora actual
    ahora = datetime.now()
    hora = ahora.strftime("%H:%M")
    
    # Nueva funcionalidad: Saludo personalizado por hora
    hora_num = ahora.hour
    if 5 <= hora_num < 12:
        saludo = "Buenos días"
    elif 12 <= hora_num < 18:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"
    
    return f"{saludo} {nombre}, son las {hora}. Bienvenido al ejemplo de Python"

if __name__ == "__main__":
    print(despedir("Maestra Sydney"))
    print(motivar("Equipo Verde"))
    print(saludar("Equipo verde"))
