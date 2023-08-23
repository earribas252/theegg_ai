
# Módulo para averiguar a cuanta altura estaría un objeto si introducimos los segundos de caída de objeto en diferentes gravedades.
def Tierra (t: int) -> float:
    gravedad = 9.8 
    h = (1/2)* gravedad * (t**2)
    return h

def Marte (t: int) -> float:
    gravedad = 3.7
    h = (1/2)* gravedad * (t**2)
    return h

def Jupiter (t: int) -> float:
    gravedad = 24.8
    h = (1/2)* gravedad * (t**2)
    return h





