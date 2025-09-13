drop database if exists SmartHomeSolutions;
create database SmartHomeSolutions;
use SmartHomeSolutions;

create table if not exists usuarios(
huella_hash binary(32) primary key not null,
nombre varchar(100) not null,
apellido varchar(100) not null,
correo_electronico varchar(100) not null);

create table if not exists dispositivos_tipo(
id int auto_increment primary key not null,
nombre varchar(100) not null);

create table if not exists ajustes(
id int auto_increment primary key not null,
dispositivos_tipo int not null,
foreign key(dispositivos_tipo) references dispositivos_tipo(id));

create table if not exists estados(
id int auto_increment primary key not null,
nombre varchar(100) not null);

create table if not exists dispositivos(
id int auto_increment primary key not null,
nombre varchar(100) not null,
tipo_id int not null,
estado_id int not null,
ubicacion varchar(100) not null,
esencial bool not null,
foreign key(tipo_id) references dispositivos_tipo(id),
foreign key(estado_id) references estados(id));

create table if not exists modos(
id int auto_increment primary key not null,
nombre varchar(100) not null);

create table if not exists roles(
id int auto_increment primary key not null,
nombre varchar(100) not null);

create table if not exists usuarios_dispositivos(
huella_usuario binary(32) not null,
id_dispositivo int not null,
primary key(huella_usuario, id_dispositivo));

