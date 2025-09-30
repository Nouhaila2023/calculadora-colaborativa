import math

def multiplicacion(a, b):
    """Multiplicar dos números"""
    return a * b

def division(a, b):
    """Dividir dos números con manejo de error"""
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(base, exponente):
    """Calcular potencia"""
    return math.pow(base, exponente)
