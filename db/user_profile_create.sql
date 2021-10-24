-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2021-10-24 12:44:13.001

-- sequences
-- Sequence: addresses_id_seq
CREATE SEQUENCE addresses_id_seq
      INCREMENT BY 1
      MINVALUE 1
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: phones_id_seq
CREATE SEQUENCE phones_id_seq
      INCREMENT BY 1
      MINVALUE 1
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: users_id_seq
CREATE SEQUENCE users_id_seq
      INCREMENT BY 1
      MINVALUE 1
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- tables
-- Table: addresses
CREATE TABLE addresses (
    id int  NOT NULL DEFAULT nextval('addresses_id_seq'),
    street varchar(60)  NOT NULL,
    address_number int  NOT NULL,
    complement varchar(60)  NOT NULL,
    city varchar(60)  NOT NULL,
    state varchar(60)  NOT NULL,
    cep varchar(60)  NOT NULL,
    user_id int  NOT NULL,
    CONSTRAINT addresses_pk PRIMARY KEY (id)
);

-- Table: phones
CREATE TABLE phones (
    id int  NOT NULL DEFAULT nextval('phones_id_seq'),
    phone_number varchar(60)  NOT NULL,
    phone_type varchar(60)  NOT NULL,
    user_id int  NOT NULL,
    CONSTRAINT phones_pk PRIMARY KEY (id)
);

-- Table: users
CREATE TABLE users (
    id int  NOT NULL DEFAULT nextval('users_id_seq'),
    name varchar(60)  NOT NULL,
    birthdate date  NOT NULL,
    email varchar(60)  NOT NULL,
    password varchar(60)  NOT NULL,
    CONSTRAINT users_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: addresses_users (table: addresses)
ALTER TABLE addresses ADD CONSTRAINT addresses_users
    FOREIGN KEY (user_id)
    REFERENCES users (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: phones_users (table: phones)
ALTER TABLE phones ADD CONSTRAINT phones_users
    FOREIGN KEY (user_id)
    REFERENCES users (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

