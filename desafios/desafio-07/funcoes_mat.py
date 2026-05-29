import math

def area_circulo(raio):
    ### Calcula a área de um círculo dado o seu raio.
    return math.pi * raio**2

def volume_esfera(raio):
    ### Calcula o volume de uma esfera dado o seu raio.
    return (4.0/3.0) * math.pi * raio**3

def hipotenusa(cateto_a, cateto_b):
    ### Calcula a hipotenusa de um triângulo retângulo dados os catetos.
    return math.hypot(cateto_a, cateto_b)
