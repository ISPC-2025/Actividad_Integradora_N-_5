import pytest
from dispositivo import Dispositivo

@pytest.fixture
def dispositivo_de_prueba():
    return Dispositivo(1, "Microondas", 1, 1, "Cocina", True)

def test_encender(dispositivo_de_prueba):
    dispositivo_de_prueba.estado_id = 1
    mensaje = dispositivo_de_prueba.encender()
    assert "Id: 1" in mensaje
    assert "Nombre: Microondas" in mensaje
    assert "Estado: 1" in mensaje
    assert "Ubicacion: Cocina" in mensaje
    assert "Esencial: Prendido" in mensaje

def test_apagar(dispositivo_de_prueba):
    dispositivo_de_prueba.estado_id = 0
    mensaje = dispositivo_de_prueba.apagar()
    assert "Id: 1" in mensaje
    assert "Nombre: Microondas" in mensaje
    assert "Estado: 1" in mensaje
    assert "Ubicacion: Cocina" in mensaje
    assert "Esencial: Apagado" in mensaje

def test_ajustar_configuracion(dispositivo_de_prueba):
    mensaje = dispositivo_de_prueba.ajustar_configuracion()
    assert "Su configuracion se guardo correctamente." == mensaje
