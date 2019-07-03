DROP TABLE IF EXISTS employee;

create table employee
(id bigint NOT NULL AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(32),
 office VARCHAR(32),
 desk_num int
 )AUTO_INCREMENT=1;
