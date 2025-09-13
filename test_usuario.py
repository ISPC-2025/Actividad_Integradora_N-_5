from usuario import Usuario

def test_registrarse():
    mi_usuario = Usuario('', 'emilse','jimenez','ej@web')
    mensaje = 'El usuario emilse jimenez con el correo electrónico ej@web se registró de manera correcta'
    assert mi_usuario.registrarse() == mensaje

def test_iniciar_sesion():
    mi_usuario = Usuario('', 'emilse','jimenez','ej@web')
    mensaje = 'Bienvenido emilse jimenez. Acabas de iniciar sesión correctamente'
    assert mi_usuario.iniciar_sesion() == mensaje

def test_cerrar_sesion():
    mi_usuario = Usuario('', 'emilse','jimenez','ej@web')
    mensaje = 'emilse has cerrado sesión'
    assert mi_usuario.cerrar_sesion() == mensaje
    