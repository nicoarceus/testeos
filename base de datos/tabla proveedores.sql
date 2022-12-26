drop table proveedor;
create table proveedor (
	id_proveedor 		serial primary key,
	nombre 				VARCHAR(100) not null,
	giro 				VARCHAR(50) not null,
	rut 				VARCHAR(50) not null,
	tipo_contribuyente 	VARCHAR (50) not null,
	direccion 			VARCHAR(100) not null,
	comuna 				VARCHAR(50) not null,
	ciudad				VARCHAR(50) not null,
	region 				VARCHAR(50) not null,
	pais 				VARCHAR(50) not null,
	movil 				Int not null,
	fono 				Int not null,
	correo_elec 		VARCHAR(50) not null,
	sitio_web 			VARCHAR(50) not null,
	categorias 			VARCHAR(50) not null,
	fecha 				date not null,
	hora 				time not null
);

