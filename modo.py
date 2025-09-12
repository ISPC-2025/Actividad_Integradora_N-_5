class Modo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def activar(self):
        '''Método que activa una automatización especifica'''
        return f'\nId: {self.id} - {self.nombre} activada\n'

    def desactivar(self):
        '''Método que desactiva una automatización especifica'''
        return f'\nId: {self.id} - {self.nombre} desactivada\n'


mi_modo = Modo(1, 'modo de ahorro de energia')


print(mi_modo.activar())
print(mi_modo.desactivar())
