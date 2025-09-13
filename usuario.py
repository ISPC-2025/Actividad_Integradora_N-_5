class Usuario:
    def __init__(self, huella, nombre, apellido, correo_electronico):
        self.__huella = huella
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo_electronico = correo_electronico

    def registrarse(self):
        #Método para que el usuario se registre
        return f'El usuario {self.__nombre} {self.__apellido} con el correo electrónico {self.__correo_electronico} se registró de manera correcta'
    
    def iniciar_sesion(self):
        #Método para que el usuario registrado inicie sesión
        return f'Bienvenido {self.__nombre} {self.__apellido}. Acabas de iniciar sesión correctamente'
    
    def cerrar_sesion(self):
        #Método de cierre de sesión
        return f'{self.__nombre} has cerrado sesión'

if __name__ == '__name__':
    mi_usuario = Usuario('','mariel','jimenez','mjim@arg.com')

    print(mi_usuario.registrarse())
    print(mi_usuario.iniciar_sesion())
    print(mi_usuario.cerrar_sesion())