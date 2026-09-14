"""Pruebas del cotizador."""
import pytest

from src.cotizador import Cotizador


def test_agregar_item_valido():
    cotizador = Cotizador()
    carrito = cotizador.agregar_item("CAM-001", 2, [])
    assert len(carrito) == 1
    assert carrito[0]["cantidad"] == 2


def test_agregar_item_sku_invalido():
    cotizador = Cotizador()
    with pytest.raises(ValueError):
        cotizador.agregar_item("XX", 1, [])


def test_calcular_subtotal():
    cotizador = Cotizador()
    carrito = [{"sku": "CAM-001", "cantidad": 2, "precio": 850.0}]
    assert cotizador.calcular_subtotal(carrito) == 1700.0


def test_cotizar_con_instalacion():
    cotizador = Cotizador()
    carrito = [{"sku": "CAM-001", "cantidad": 1, "precio": 850.0}]
    resumen = cotizador.cotizar(carrito)
    assert resumen["subtotal"] == 850.0
    assert resumen["instalacion"] == 350.0
    assert resumen["total"] == pytest.approx(1392.0)


def test_cotizar_descuento_invalido():
    cotizador = Cotizador()
    with pytest.raises(ValueError):
        cotizador.cotizar([], descuento=50)
