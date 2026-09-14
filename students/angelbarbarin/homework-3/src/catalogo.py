import json
import os
from typing import List

PRODUCTOS = [
    {"sku": "CAM-001", "nombre": "Camara de reversa universal", "precio": 850.0, "categoria": "camara"},
    {"sku": "CAM-002", "nombre": "Camara de reversa con guias dinamicas", "precio": 1450.0, "categoria": "camara"},
    {"sku": "PAN-007", "nombre": "Pantalla 7 pulgadas touch", "precio": 2300.0, "categoria": "pantalla"},
    {"sku": "PAN-010", "nombre": "Pantalla 10 pulgadas Android Auto", "precio": 4900.0, "categoria": "pantalla"},
    {"sku": "SEN-004", "nombre": "Kit 4 sensores de reversa", "precio": 1200.0, "categoria": "sensor"},
]

COSTO_INSTALACION = {"camara": 350.0, "pantalla": 600.0, "sensor": 450.0}


class Catalogo:  

    def __init__(self, productos=PRODUCTOS):
        self.productos = productos

    def ObtenerProducto(self, sku):
        for p in self.productos:
            if p["sku"] == sku:
                return p
        return None

    def listar_por_categoria(self, categoria):
        resultado = []
        for p in self.productos:
            if p["categoria"] == categoria:
                resultado.append(p)
        return resultado

    def precio_instalacion(self, sku):
        producto = self.ObtenerProducto(sku)
        if producto == None:
            return 0.0
        return COSTO_INSTALACION[producto["categoria"]]

    def exportar_json(self, ruta):
        f = open(ruta, "w")
        f.write(json.dumps(self.productos))
        f.close()
