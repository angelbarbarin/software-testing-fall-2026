from src.catalogo import Catalogo
from src.validaciones import validar_cantidad, validar_descuento, validar_sku

IVA = 0.16


class Cotizador:

    def __init__(self, catalogo=None):
        if catalogo == None:
            catalogo = Catalogo()
        self.catalogo = catalogo

    def agregar_item(self, sku, cantidad, carrito=[]):
        if not validar_sku(sku):
            raise ValueError("SKU invalido")
        if not validar_cantidad(cantidad):
            raise ValueError("Cantidad invalida")
        producto = self.catalogo.ObtenerProducto(sku)
        if producto == None:
            raise ValueError("Producto no encontrado")
        carrito.append({"sku": sku, "cantidad": int(cantidad), "precio": producto["precio"]})
        return carrito

    def calcular_subtotal(self, carrito):
        subtotal = 0.0
        for item in carrito:
            subtotal = subtotal + item["precio"] * item["cantidad"]
        return subtotal

    def calcular_instalacion(self, carrito):
        total = 0.0
        for item in carrito:
            total = total + self.catalogo.precio_instalacion(item["sku"]) * item["cantidad"]
        return total

    def cotizar(self, carrito, descuento=0, incluir_instalacion=True, cliente=None):
        if not validar_descuento(descuento):
            raise ValueError("Descuento invalido")
        subtotal = self.calcular_subtotal(carrito)
        instalacion = 0.0
        if incluir_instalacion:
            instalacion = self.calcular_instalacion(carrito)
        base = subtotal + instalacion
        ahorro = base * (descuento / 100.0)
        base_con_descuento = base - ahorro
        impuesto = base_con_descuento * IVA
        total = base_con_descuento + impuesto
        resumen = {"subtotal": subtotal, "instalacion": instalacion, "descuento": ahorro, "iva": impuesto, "total": total}
        return resumen
