class Modo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def activar(self):
        '''Método que activa una automatización especifica'''
        return 'Automatización activada\n'

    def desactivar(self):
        '''Método que desactiva una automatización especifica'''
        return 'Automatización desactivada\n'
