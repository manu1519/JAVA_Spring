create database prueba;

use prueba;

create table Usuario(id int, email varchar(255), username varchar(50));

alter table Usuario add edad int;

alter table Usuario drop column edad;

alter table Usuario modify column email varchar(50);

alter table Usuario modify column id int auto_increment;

insert into Usuario(email, username, edad)
values ("g.bell@hotmail.com","Gabriela",27);

select * FROM Usuario where edad<30;

update Usuario set edad = 26 where id="1";

delete from Usuario where id="3";