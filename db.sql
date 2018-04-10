create  database db;

use db;

create table complaintform(
ID int NOT NULL AUTO_INCREMENT,
issuearea varchar(25),
postdate date,
complaint varchar(50),
priority varchar(5),
PRIMARY KEY (ID)
);

insert into db.complaintform(issuearea,postdate,complaint,priority)  values('delhi', '2018-11-11', 'Enhanced security in the area', 'LOW');
insert into db.complaintform(issuearea,postdate,complaint,priority)  values('east delhi', '2018-02-02', 'Festive celebrations in the society', 'LOW');
insert into db.complaintform(issuearea,postdate,complaint,priority)  values('east noida', '2018-02-01', 'No parking facilities in the area', 'LOW');
insert into db.complaintform(issuearea,postdate,complaint,priority)  values('delhi', '2018-11-11', 'Fights between children in mainarea', 'LOW');
insert into db.complaintform(issuearea,postdate,complaint,priority)  values('delhi', '2018-11-11', 'No cleaning check of swimming pool of area', 'LOW');
insert into db.complaintform(issuearea,postdate,complaint,priority)  values('delhi', '2018-11-11', 'No power supply cut in the area', 'LOW');
insert into db.complaintform(issuearea,postdate,complaint,priority)  values('delhi', '2018-11-11', 'Need proper management', 'LOW');


select * from db.complaintform;

UPDATE complaintform SET priority = 'LOW' where priority='HIGH'

drop database db;