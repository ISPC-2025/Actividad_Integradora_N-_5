insert into usuarios (huella_hash, nombre, apellido, correo_electronico) values
(0xA1B2C3D4E5F60718293A4B5C6D7E8F90112233445566778899AABBCCDDEEFF00, 'Juan', 'Pérez', 'juan.perez1990@gmail.com'),
(0xB2C3D4E5F60718293A4B5C6D7E8F90112233445566778899AABBCCDDEEFF0011, 'María', 'González', 'maria.gonzalez87@yahoo.com'),
(0xC3D4E5F60718293A4B5C6D7E8F90112233445566778899AABBCCDDEEFF001122, 'Luis', 'Rodríguez', 'luis.rodriguez@outlook.com'),
(0xD4E5F60718293A4B5C6D7E8F90112233445566778899AABBCCDDEEFF00112233, 'Ana', 'López', 'ana.lopez23@hotmail.com'),
(0xE5F60718293A4B5C6D7E8F90112233445566778899AABBCCDDEEFF0011223344, 'Carlos', 'Martínez', 'cmartinez.work@protonmail.com'),
(0xF60718293A4B5C6D7E8F90112233445566778899AABBCCDDEEFF001122334455, 'Laura', 'Ramírez', 'laura.ramirez.uni@edu.ar'),
(0x0718293A4B5C6D7E8F90112233445566778899AABBCCDDEEFF00112233445566, 'Pedro', 'Fernández', 'pedro.fernandez85@icloud.com'),
(0x18293A4B5C6D7E8F90112233445566778899AABBCCDDEEFF0011223344556677, 'Sofía', 'Torres', 'sofia.torres92@live.com'),
(0x293A4B5C6D7E8F90112233445566778899AABBCCDDEEFF001122334455667788, 'Diego', 'Castro', 'd.castro.dev@gmail.com'),
(0x3A4B5C6D7E8F90112233445566778899AABBCCDDEEFF00112233445566778899, 'Elena', 'Morales', 'elena_morales@empresa.mx'),
(0x4B5C6D7E8F90112233445566778899AABBCCDDEEFF00112233445566778899AA, 'Gabriel', 'Vargas', 'gabriel.vargas.dev@outlook.com'),
(0x5C6D7E8F90112233445566778899AABBCCDDEEFF00112233445566778899AABB, 'Valeria', 'Ruiz', 'valeria.ruiz@hotmail.com');

insert into dispositivos_tipo (nombre) values
('Sensor'),
('Cámara de seguridad'),
('Servidor'),
('Red');

insert into estados (nombre) values
('Encendido'),
('Apagado');

insert into dispositivos (nombre, tipo_id, estado_id, ubicacion, esencial) values
('Sensor de temperatura - Sala de Servidores', 1, 1, 'Data Center - Rack A1', true),
('Sensor de humo - Almacén Principal', 1, 2, 'Almacén Principal - Zona Norte', true),
('Sensor de movimiento - Oficina Piso 3', 1, 1, 'Edificio Central - Piso 3', false),
('Cámara de seguridad - Entrada Principal', 2, 1, 'Edificio Central - Acceso Principal', true),
('Cámara de seguridad - Estacionamiento Subterráneo', 2, 2, 'Estacionamiento Nivel -1', false),
('Cámara de seguridad - Recepción', 2, 1, 'Edificio Central - Lobby', true),
('Servidor de aplicaciones - App01', 3, 1, 'Data Center - Rack B2', true),
('Servidor de base de datos - DB01', 3, 1, 'Data Center - Rack B3', true),
('Servidor de respaldo - Backup01', 3, 1, 'Data Center - Rack C1', true),
('Servidor de pruebas - Dev01', 3, 2, 'Data Center - Rack D4', false),
('Router principal - CoreRouter01', 4, 1, 'Sala de Redes - Rack 1', true),
('Switch de red - Switch01', 4, 1, 'Edificio Central - Piso 2', true);

select * from usuarios;

select * from dispositivos where esencial = 1;

select * from dispositivos_tipo where nombre != 'Red';

select nombre from estados