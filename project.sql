create database db;
use db;

create table Bookmarks(

id varchar(3),
login varchar(30),
postdate date,
issuearea varchar(25),

complaint varchar(50),

status varchar(10)


);


drop table db.submissions 

create table complaintform(
id int not null auto_increment,
person varchar(30),
issuearea varchar(25),
postdate date,
complaint varchar(50),
flagValue int,
priority varchar(15), 
status varchar(10),
email varchar(30),
primary key(id)
);

create table user(
id int not null auto_increment,
name varchar(30),
email varchar(30),
password varchar(30),
phone int(11),
primary key(id)
);

UPDATE complaintform SET priority ='Unspecified' where priority="HIGH"

select * from db.user;

select * from db.complaintform;

delete from db.complaintform;

create table Submissions(
id int,
login varchar(30),
postdate date,
issuearea varchar(25),
complaint varchar(50),
status varchar(10)

); 

drop table db.submissions

desc db;

