class Dispositivo:
    def __init__(self, id, nombre, tipo_id, estado_id, ubicacion, esencial):
        self.id = id
        self.nombre = nombre
        self.tipo_id = tipo_id
        self.estado_id = estado_id
        self.ubicacion = ubicacion
        self.esencial = esencial

    def encender(self):
        return "El dispositivo esta encendido."
    
    def apagar(self):
        return "El dispositivo se apagó."
    
    def ajustar_configuracion(self):
        return "Su configuracion se guardo correctamente."
    
mi_dispositivo = Dispositivo(1, "Microondas", "Electrodomestico", "Apagado", "Cocina", True)

print(mi_dispositivo.encender())
print(mi_dispositivo.apagar())
print(mi_dispositivo.ajustar_configuracion())