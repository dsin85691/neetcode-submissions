CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    balance INTEGER,
    name TEXT,
    status TEXT
);

INSERT INTO bank_accounts (balance, name) VALUES
(8000, 'Alice'),
(9000, 'Bob'),
(12000, 'Charlie'),
(40000, 'David'),
(5000, 'Eve'),
(60000, 'Frank');
-- Do not modify above this line. --

UPDATE bank_accounts SET status = 'VIP' WHERE balance > 10000 AND balance < 100000; 
SELECT id, balance, status FROM bank_accounts WHERE balance > 10000 AND balance < 100000;  




