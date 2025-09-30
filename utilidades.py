def validar_numero(entrada):
    """Validar que la entrada sea un número"""
    try:
        return float(entrada)
    except ValueError:
        return None

def mostrar_menu():
    """Mostrar menú de opciones"""
    print("\n=== MENÚ CALCULADORA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("0. Salir")

def limpiar_pantalla():
    """Limpiar la pantalla de la consola"""
    import os
    os.system("cls" if os.name == "nt" else "clear")
