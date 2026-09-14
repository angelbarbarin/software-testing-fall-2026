"""Pruebas del catalogo de productos."""
from src.catalogo import Catalogo


def test_obtener_producto_existente():
    catalogo = Catalogo()
    producto = catalogo.ObtenerProducto("CAM-001")
    assert producto is not None
    assert producto["precio"] == 850.0


def test_obtener_producto_inexistente():
    catalogo = Catalogo()
    assert catalogo.ObtenerProducto("NO-EXISTE") is None


def test_listar_por_categoria():
    catalogo = Catalogo()
    pantallas = catalogo.listar_por_categoria("pantalla")
    assert len(pantallas) == 2


def test_precio_instalacion():
    catalogo = Catalogo()
    assert catalogo.precio_instalacion("PAN-007") == 600.0
    assert catalogo.precio_instalacion("NO-EXISTE") == 0.0
