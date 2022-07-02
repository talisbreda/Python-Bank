create database trabalho;
use trabalho;

create table client (
	idClient int not null primary key auto_increment,
    passcode varchar(45) not null,
    fullname varchar(255) not null,
    email varchar(255) not null,
    phone varchar(30) not null,
    cpf int not null,
    rg int not null
);

create table account (
	idAccount int not null primary key auto_increment,
    holder int not null,
    accNumber int not null,
    agency int not null,
    accType int not null,
    foreign key (holder) references client (idClient)
);

select