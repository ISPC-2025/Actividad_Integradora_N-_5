class Dispositivo:
    def __init__(self, id, nombre, tipo_id, estado_id, ubicacion, esencial):
        self.id = id
        self.nombre = nombre
        self.tipo_id = tipo_id
        self.estado_id = estado_id
        self.ubicacion = ubicacion
        self.esencial = esencial

    def encender(self):
        return f"\nId: {self.id} - Nombre: {self.nombre} - Tipo: {self.tipo_id} - Estado: { '1' if self.estado_id == True else '0'} - Ubicacion: {self.ubicacion} - Esencial: {'Prendido' if self.esencial == True else 'Apagado'}"
    
    def apagar(self):
        return f"\nId: {self.id} - Nombre: {self.nombre} - Tipo: {self.tipo_id} - Estado: {'0' if self.estado_id == True else '1'} - Ubicacion: {self.ubicacion} - Esencial: {'Apagado' if self.esencial == True else 'Prendido'}"
    
    def ajustar_configuracion(self):
        return "\nSu configuracion se guardo correctamente."
    
mi_dispositivo = Dispositivo(1, "Microondas", 1, 1, "Cocina", True)

print(mi_dispositivo.encender())
print(mi_dispositivo.apagar())
print(mi_dispositivo.ajustar_configuracion())