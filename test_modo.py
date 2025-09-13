'''
python -m pip install pytest
'''

from modo import Modo


def test_activar():
    nueva_prueba = Modo(1, 'modo de ahorro de energia')
    assert nueva_prueba.activar(
    ) == f'\nId: {nueva_prueba.id} - {nueva_prueba.nombre} activada\n'

def test_desactivar():
    nueva_prueba = Modo(1, 'modo de ahorro de energia')
    assert nueva_prueba.activar(
    ) == f'\nId: {nueva_prueba.id} - {nueva_prueba.nombre} activada\n'
