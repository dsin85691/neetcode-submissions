CREATE TYPE account_type AS ENUM ('checking', 'savings', 'cd', 'money_market');  


CREATE TABLE bank_accounts ( 
    id INTEGER PRIMARY KEY, 
    account_type account_type, 
    balance INTEGER
); 

-- Do not modify below this line --
INSERT INTO bank_accounts (id, account_type, balance) VALUES 
  (1, 'checking', 1000),
  (2, 'savings', 2000),
  (3, 'cd', 3000),
  (4, 'money_market', 4000);

SELECT 
    ba.*,
    (SELECT STRING_AGG(column_name || ' ' || data_type, ', ')
     FROM information_schema.columns 
     WHERE table_name = 'bank_accounts') AS column_types
FROM 
    bank_accounts ba;
