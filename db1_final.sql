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


create table complaintform(
complaint_id int not null auto_increment,
person varchar(30),
issuearea varchar(25),
postdate date,
complaint varchar(50),
priority varchar(15), 
status varchar(10),
email varchar(30),
primary key(complaint_id)
);

create table usern(
id int not null auto_increment,
name varchar(30),
email varchar(30),
password varchar(30),
phone long,
address varchar(50),
gender varchar(5),
primary key(id)
);


create table Submissions(
id int,
login varchar(30),
postdate date,
issuearea varchar(25),
complaint varchar(50),
status varchar(10)

); 


