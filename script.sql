use Sopes1;

CREATE TABLE Usuario(
id int not null auto_increment,
nombre varchar(200) ,
usuario varchar(40) not null,
contraseña varchar(15) not null,
PRIMARY KEY(id)
); 


insert into Usuario(nombre,usuario,contraseña) values('Carlos Hernandez','carlos123','1234');
insert into Usuario(nombre,usuario,contraseña) values('Andres Carvajal','andres123','1234');
insert into Usuario(nombre,usuario,contraseña) values('Selvin ','selvin123','1234');
insert into Usuario(nombre,usuario,contraseña) values('Herbert Reyes','herbert123','1234');
