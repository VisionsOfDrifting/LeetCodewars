/*
create table duplicate_emails( 
   Id INT(2), 
   Email VARCHAR(128));

insert into duplicate_emails(Id, Email) Values(1,'a@b.com');
insert into duplicate_emails(Id, Email) Values(2,'c@d.com');
insert into duplicate_emails(Id, Email) Values(3,'a@b.com');
*/

SELECT Email 
FROM duplicate_emails 
GROUP BY Email 
HAVING count(*)>1;
