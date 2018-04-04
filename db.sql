drop database TESTDB ;

create database TESTDB;

use TESTDB;


create table employee(
pname varchar(35),
problem varchar(50),
priority varchar(5)
);

			

select * from TESTDB.employee;

insert into TESTDB.employee values("Akarsh Srivastava",
"No water supply from Monday","LOW");
insert into TESTDB.employee values("Anushka Gupta",
"Improved parking facilities in the area","LOW");


    