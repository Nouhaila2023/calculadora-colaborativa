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

def raiz_cuadrada(numero):
    """Calcular raíz cuadrada"""
    if numero < 0:
        return "Error: No se puede calcular raíz de número negativo"
    return math.sqrt(numero)

def factorial(n):
    """Calcular factorial de un número"""
    if n < 0:
        return "Error: No existe factorial de números negativos"
    return math.factorial(int(n))
