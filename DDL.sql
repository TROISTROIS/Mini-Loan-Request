CREATE DATABASE dbLoan;

CREATE TABLE IF NOT EXISTS tbloan (
id VARCHAR(10),
name VARCHAR(50),
email VARCHAR(20),
phone_number VARCHAR(20),
CONSTRAINT pkey PRIMARY KEY(id, phone_number));

CREATE TYPE status AS ENUM ('PENDING','APPROVED','REJECTED');
CREATE TABLE IF NOT EXISTS tbLoanRequest(
id VARCHAR(10),
user_id VARCHAR(20),
amount DECIMAL,
status status,
reason VARCHAR(300),
created_at TIMESTAMP,
updated_at TIMESTAMP,
CONSTRAINT pkey2 PRIMARY KEY(id, user_id));


SELECT * FROM tbLoanRequest;

