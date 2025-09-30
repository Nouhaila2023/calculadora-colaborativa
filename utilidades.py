import datetime

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
    print("6. Raíz cuadrada")
    print("7. Factorial")
    print("0. Salir")

def limpiar_pantalla():
    """Limpiar la pantalla de la consola"""
    import os
    os.system("cls" if os.name == "nt" else "clear")

def registrar_operacion(operacion, resultado):
    """Registrar operación en el historial"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("historial.txt", "a") as f:
        f.write(f"[{timestamp}] {operacion} = {resultado}\n")

def mostrar_resultado(operacion, resultado):
    """Mostrar resultado con formato"""
    print(f"\n{=*40}")
    print(f"Operación: {operacion}")
    print(f"Resultado: {resultado}")
    print(f"{=*40}")
