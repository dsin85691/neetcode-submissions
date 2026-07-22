CREATE TYPE account_type AS ENUM ('checking', 'savings', 'cd', 'money_market');

CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY,
    account_type account_type,
    balance INTEGER
);
-- Do not modify above this line --

INSERT INTO bank_accounts VALUES 
(1, 'checking', 1000), 
(2, 'savings', 2000), 
(3, 'cd', 3000), 
(4, 'money_market', 4000); 








-- Do not modify below this line --
SELECT * FROM bank_accounts;
