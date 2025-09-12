class Usuario:
    def __init__(self, huella, nombre, apellido, correo_electronico):
        self.huella = huella
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico

    def registrarse(self):
        #Método para que el usuario se registre
        return 'Registro existoso'
    
    def iniciar_sesion(self):
        #Método para que el usuario registrado inicie sesión
        return 'Inició sesión correctamente'
    
    def cerrar_sesion(self):
        #Método de cierre de sesión
        return 'Sesión cerrada'
    
mi_usuario = Usuario('','mariel','jimenez','mjim@arg.com')

print(mi_usuario.registrarse())
print(mi_usuario.iniciar_sesion())
print(mi_usuario.cerrar_sesion())