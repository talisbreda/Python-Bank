create database trabalho;
use trabalho;

create table client (
	idClient bigint not null primary key auto_increment,
    passcode varchar(255) not null,
    fullname varchar(255) not null,
    email varchar(255) not null,
    phone varchar(30) not null,
    cpf bigint not null,
    rg bigint not null
);

create table account (
	idAccount int not null primary key auto_increment,
    holder bigint not null,
    accNumber int not null,
    agency int not null,
    accType int not null,
    foreign key (holder) references client (idClient)
);

select * from client;
select * from account;