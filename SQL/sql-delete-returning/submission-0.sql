CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,
    balance INTEGER,
    last_transaction_date DATE
);

INSERT INTO bank_accounts (name, balance, last_transaction_date) VALUES
    ('Alice', 1000, '2023-11-30'),
    ('Bob', -100, '2023-12-31'),
    ('Charlie', 2000, '2024-01-03'),
    ('David', -500, '2024-01-04'),
    ('Eve', 1500, '2024-01-05');
-- Do not modify above this line. --



DELETE FROM bank_accounts WHERE balance < 0 AND last_transaction_date < '2024-01-01' RETURNING id, name; 

