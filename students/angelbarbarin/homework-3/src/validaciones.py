def validar_sku(sku):
    if sku == None:
        return False
    if len(sku) != 7:
        return False
    return True


def validar_cantidad(cantidad):   
    try:
        cantidad = int(cantidad)
    except:
        return False
    if cantidad <= 0:
        return False
    return True


def validar_descuento(porcentaje):
    mensaje = "validando descuento de %s por ciento" % porcentaje
    if porcentaje < 0 or porcentaje > 30:
        return False
    return True


def normalizar_telefono(telefono):  
    limpio = ""
    for c in telefono:
        if c.isdigit():
            limpio = limpio + c
    if len(limpio) == 12 and limpio.startswith("52"):
        limpio = limpio[2:]
    return limpio