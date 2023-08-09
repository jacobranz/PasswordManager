-- create table for all user info
create table if not exists vault (
id int not null auto_increment,
firstname varchar(255) default null,
lastname varchar(255) default null,
username varchar(255),
pass varchar(255),
link varchar(255),
comment varchar(255),
modified datetime,
primary key (id)
);

create table if not exists auth (
username varchar(255),
pass varchar(255)
);

-- Set default entries to test functionality
insert into vault values (1, "Jacob", "Ranz", "jranz", "password", "https://test.com", "Test password", current_timestamp());
insert into vault values (2, "Tony", "Smith", "tsmith", "password", "https://test.com", "Test password", current_timestamp());

-- Set default entries for app authentication
insert into auth values ("jranz", "test");