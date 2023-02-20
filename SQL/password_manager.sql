create table if not exists vault (
id int not null auto_increment,
firstname varchar(255) default null,
lastname varchar(255) default null,
username varchar(255),
password varchar(255),
comment varchar(255),
modified datetime,
primary key (id)
);

-- Set default entries to test functionality
insert into vault values (1, "Jacob", "Ranz", "jranz", "password", "Test password", current_timestamp());
insert into vault values (2, "Tony", "Smith", "tsmith", "password", "Test password", current_timestamp());