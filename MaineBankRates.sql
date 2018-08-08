create database MaineBankRates;

use MaineBankRates;

create table deposit_rates (
    id bigint not null auto_increment,
    institution_id bigint not null,
    type varchar(50) not null,
    min_balance varchar(50) not null,
    interest_rate varchar(20) not null,
    apr varchar(20) not null,
    creation_date DATETIME NOT NULL DEFAULT  CURRENT_TIMESTAMP,
    activity_date DATETIME NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cleaned int(1) NOT NULL DEFAULT 0,
    primary key (id)
);


create table loan_rates (
    
);


create table institution (
    id bigint not null auto_increment,
    name varchar(20) not null,
    website varchar(50) not null,
    creation_date DATETIME NOT NULL DEFAULT  CURRENT_TIMESTAMP,
    activity_date DATETIME NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cleaned int(1) NOT NULL DEFAULT 0,
    primary key (id)
);


-- starter institutions
insert into institution (name,website) values ('Androscoggin Bank','https://www.androscogginbank.com');
insert into institution (name,website) values ('Norway Savings Bank','https://www.norwaysavingsbank.com');
insert into institution (name,website) values ('Bangor Savings Bank','https://www.bangord.com');